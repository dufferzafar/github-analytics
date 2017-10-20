
# Hadoop + Spark
export HADOOP_HOME=/usr/local/hadoop
export SPARK_HOME=/usr/local/spark
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64

# for pseudo distributed mode
export HADOOP_MAPRED_HOME=$HADOOP_HOME
export HADOOP_COMMON_HOME=$HADOOP_HOME
export HADOOP_HDFS_HOME=$HADOOP_HOME
export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native
export HADOOP_INSTALL=$HADOOP_HOME

export YARN_HOME=$HADOOP_HOME

export PATH=$PATH:$HADOOP_HOME/sbin:$HADOOP_HOME/bin:$SPARK_HOME/bin
