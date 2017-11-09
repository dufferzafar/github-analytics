
#

commits = utils.read_csv(spark, "hdfs:/commits_new.csv")
projects = utils.read_csv(spark, "hdfs:/projects_new.csv")

commits.createOrReplaceTempView("commits")
projects.createOrReplaceTempView("projects")

q = """
    SELECT C.project_id as project_id, COUNT(*) as total_commits_by_others
    FROM commits as C, projects as P
    WHERE C.project_id = P.id
    AND C.author_id <> P.owner_id
    GROUP BY C.project_id
"""

res = spark.sql(q)

res.write.csv(
    "hdfs:/project_commit_others_count",
#     mode="overwrite",
    nullValue="\\N"
)

# Number of commits of a user made on repositories not owned by them

q = """
    SELECT C.author_id as user_id,
           COUNT(*) as total_commits_on_other_repos

    FROM commits as C, projects as P

    WHERE C.project_id = P.id
    AND C.author_id <> P.owner_id

    GROUP BY C.author_id
"""

res = spark.sql(q)

res.write.csv(
    "hdfs:/user_commit_others_count",
#     mode="overwrite",
    nullValue="\\N"
)

#

user_more = utils.read_csv(spark, "hdfs:/user_more.csv")
users = utils.read_csv(spark, "hdfs:/users.csv")

users = (
    users
    .withColumnRenamed("id", "user_id")
    .select("user_id", "login", "company", "type", "fake", "deleted")
)

user_new = users.join(user_more, "user_id", "left")

# Torvalds is at the top
# most_followers = user_new.orderBy("followers", ascending=False)

# most_followers.show()
top = (
    user_new
    .where(
        (user_new.type == "USR")
        & (user_new.followers.isNotNull())
#         & (user_new.starred.isNotNull())
    )
    .orderBy("followers", ascending=False)
)

top.show(50)

top_users = [5203, 896, 376498, 6240, 1779, 9236, 1570, 3871, 1736, 13009, 24452, 616741, 2468643, 2427, 81423, 796, 10005, 417948, 2016667, 1954]

# top_users = top_users[:1]

res = (
    commits
    .where(
        commits.created_at.isNotNull()
    # IDs of top 20 peeps
        commits.author_id.isin(top_users)
    )
    .select(
        F.date_format('created_at', 'E').alias('day'),
        F.hour('created_at').alias('hour')
    )
   .groupBy(
    'user'
    'day',
    'hour'
   )
   .count()
)

res.write.csv(
    "hdfs:/top_users_commit_punchcard"
)

