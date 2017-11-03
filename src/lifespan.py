# path to folder containing all csvs is given as command line argument

import json
import sys

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField
import pyspark.sql.types as spark_types
import pyspark.sql.functions as sf


def spark_schema_from_json(j):
    return StructType([
        StructField(
            f["name"],
            spark_types._parse_datatype_string(f.get("type", "string")),
            f.get("nullable", True),
            f.get("metadata", None)
        )
        for f in j
    ])

spark = SparkSession.builder.master("local").appName("GH Users").getOrCreate()

with open("ghtorrent-schema.json") as f:
    db_schema = json.load(f)


path_to_data = sys.argv[1]
assert(path_to_data)

# Read projects.csv
df_projects = spark.read.csv(
    path=path_to_data+"projects.csv",
    schema=spark_schema_from_json(db_schema["projects.csv"]),
    nullValue="\\N",
)



# Read issues.csv
df_issues = spark.read.csv(
    path=path_to_data+"issues.csv",
    schema=spark_schema_from_json(db_schema["issues.csv"]),
    nullValue="\\N",
)



# Read commits.csv
df_commits = spark.read.csv(
    path=path_to_data+"commits.csv",
    schema=spark_schema_from_json(db_schema["commits.csv"]),
    nullValue="\\N",
)



# Read pull_requests.csv
df_pull_requests = spark.read.csv(
    path=path_to_data+"pull_requests.csv",
    schema=spark_schema_from_json(db_schema["pull_requests.csv"]),
    nullValue="\\N",
)



# Read pull_request_history.csv
df_pull_request_history = spark.read.csv(
    path=path_to_data+"pull_request_history.csv",
    schema=spark_schema_from_json(db_schema["pull_request_history.csv"]),
    nullValue="\\N",
)


# # Lifespan of projects based on commits


# first and last commit per project
df_commits.createOrReplaceTempView("temp")
query = """
        SELECT project_id,
               min(created_at) as first,
               max(created_at) as last
        FROM temp
        WHERE
          created_at < CURRENT_TIMESTAMP
          AND project_id IS NOT NULL
        GROUP BY project_id
        """

lifespan_commits = spark.sql(query)


lifespan_commits = lifespan_commits.withColumn('duration', sf.datediff(sf.col("last"), sf.col("first"))) \
                                   .select("project_id", "duration").sort(sf.desc("duration"))
# lifespan_commits.show()


# # Lifespan of projects based on issues


# first and last issue per project
df_issues.createOrReplaceTempView("temp")
query = """
        SELECT  repo_id as project_id,
                min(created_at) as first,
                max(created_at) as last
        FROM temp
          WHERE created_at < CURRENT_TIMESTAMP
                AND repo_id IS NOT NULL
        GROUP BY repo_id
        """
lifespan_issues = spark.sql(query)

lifespan_issues = lifespan_issues.withColumn('duration', sf.datediff(sf.col("last"), sf.col("first"))) \
                                 .select("project_id", "duration").sort(sf.desc("duration"))
# lifespan_issues.show()


# # Lifespan of project based on pull request activity


# last action of each pull request
last_act_plreq = df_pull_request_history.groupBy(df_pull_request_history.pull_request_id) \
                                        .agg(sf.max(df_pull_request_history.created_at).alias('last_action_time')) \
                                        .sort(sf.desc("last_action_time"))
# last_act_plreq.show()



df1 = df_pull_requests.alias("df1")
df2 = last_act_plreq.alias("df2")

# last action of pull request per (base repo, head repo)
df_temp = df1.join(df2, sf.col("df1.id") == sf.col("df2.pull_request_id"), "inner") \
            .select(df1.head_repo_id, df1.base_repo_id,df2.last_action_time) \
            .where(df1.head_repo_id.isNotNull() & df1.base_repo_id.isNotNull()) \
            .sort(sf.desc("last_action_time"))

# df_temp.show()



df_temp.createOrReplaceTempView("temp")

# takes two passes need to do in single pass
query = """ 
            SELECT temp.head_repo_id as project_id, temp.last_action_time 
            FROM temp WHERE temp.head_repo_id IS NOT NULL
            UNION ALL
            SELECT temp.base_repo_id as project_id, temp.last_action_time 
            FROM temp WHERE temp.base_repo_id IS NOT NULL
        """
# last pull activity per repo
last_pull_act_repo = spark.sql(query)
# last_pull_act_repo.show()



# first and last pull_request activity
last_pull_act_repo.createOrReplaceTempView("temp")
lifespan_pulls = spark.sql("""SELECT project_id,
                      min(last_action_time) as first,
                      max(last_action_time) as last
                      FROM temp
                      WHERE last_action_time < CURRENT_TIMESTAMP
                      AND project_id IS NOT NULL
                      GROUP BY project_id
                      """
                           )
lifespan_pulls = lifespan_pulls.withColumn('duration', sf.datediff(sf.col("last"), sf.col(
    "first")))                    .select("project_id", "duration").sort(sf.desc("duration"))
# lifespan_pulls.show()


# # Lifespan single table


df_projects.createOrReplaceTempView("temp")
lifespan_commits.createOrReplaceTempView("t1")
lifespan_issues.createOrReplaceTempView("t2")
lifespan_pulls.createOrReplaceTempView("t3")

query = """
    SELECT temp.id as project_id, temp.url, temp.owner_id, temp.language,
           t1.duration as `commits(days)`, t2.duration as `issues(days)`, t3.duration as `pull_requests(days)`
    FROM temp, t1, t2, t3
    WHERE temp.id == t1.project_id AND t1.project_id == t2.project_id AND t2.project_id == t3.project_id
    AND temp.language is NOT NULL
"""

lifespan = spark.sql(query)
# lifespan.show()


# # Average Lifespan of a project and project language
lifespan.createOrReplaceTempView("temp")
query = """
    SELECT language, ROUND(AVG(`commits(days)`), 5) as avglife_commits,
           ROUND(AVG(`issues(days)`), 5) as avglife_issues,
           ROUND(AVG(`pull_requests(days)`), 5) as avglife_pull_requests
    FROM temp
    GROUP BY language
    ORDER BY language
"""
lifespan_lang = spark.sql(query)
# lifespan_lang.show()



lifespan_lang.coalesce(1).write.json("avg-lifespan-per-language")
