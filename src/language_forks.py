from pyspark.sql import SparkSession

from utils import spark_schema_from_json, load_schema

spark = SparkSession.builder.master("spark://vm1:7077").appName("Language_forks").getOrCreate()

db_schema = load_schema()

df_projects = spark.read.csv(
    # path="/home/hthuwal/Desktop/Ghtorrent_heads/projects.csv",
    # schema=spark_schema_from_json(db_schema["projects.csv"]),
    path="hdfs:/projects.csv",
    schema=spark_schema_from_json(db_schema["projects_new.csv"]),
    multiLine=True,
    nullValue="\\N",
)

# df = df_projects.where(df_projects.forked_from.isNotNull()).groupBy(df_projects.language).agg(sf.count().alias('num_forks')).sort(df_projects.num_forks.desc())
df_projects.createOrReplaceTempView("temp")
query = """
        SELECT language, count(*) as num_forks
        FROM temp
        WHERE forked_from is NOT NULL AND language is NOT NULL
        GROUP BY language
        ORDER BY num_forks DESC
"""
df = spark.sql(query)
df.coalesce(1).write.json("Language_forks", mode="overwrite")

# spark-submit --master spark://vm1:7077 --deploy-mode client --executor-memory 3G --driver-memory 4G --conf spark.driver.maxResultSize=3g language_forks.py 
