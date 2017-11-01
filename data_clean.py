from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext

conf = SparkConf().setAppName("Clean")

# create a SQLContext
sc = SQLContext(SparkContext(conf=conf))

path = "/home/hthuwal/Desktop/Ghtorrent_heads"
# read file into rdd
df = sc.read.csv(path+"/projects.csv")

# drop 4th column
df = df.drop("_c3")

# save the modified table, this works but saves each partition of the data, i.e
# 5 RDDs seperately in a folder
df.write.csv(path+"/projects_new.csv")
