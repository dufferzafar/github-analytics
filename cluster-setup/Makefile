MY_IP := $(shell ifconfig wlp2s0 | grep "inet addr:" | cut -d: -f2 | cut -d " " -f 1)

stop-all: stop-hdfs stop-spark
start-all: start-hdfs start-spark

start-hdfs:
	./run vm1 "~/hadoop/sbin/hadoop-daemon.sh" start namenode

	./run vm2 "~/hadoop/sbin/hadoop-daemon.sh" start datanode
	./run vm3 "~/hadoop/sbin/hadoop-daemon.sh" start datanode
	./run vm4 "~/hadoop/sbin/hadoop-daemon.sh" start datanode

stop-hdfs:
	./run vm1 "~/hadoop/sbin/hadoop-daemon.sh" stop namenode

	./run vm2 "~/hadoop/sbin/hadoop-daemon.sh" stop datanode
	./run vm3 "~/hadoop/sbin/hadoop-daemon.sh" stop datanode
	./run vm4 "~/hadoop/sbin/hadoop-daemon.sh" stop datanode

start-spark:
	./run vm1 "~/spark/sbin/start-master.sh" -h vm1

	./run vm2 "~/spark/sbin/start-slave.sh" -c 4 -m 3500M spark://vm1:7077
	./run vm3 "~/spark/sbin/start-slave.sh" -c 4 -m 3500M spark://vm1:7077
	./run vm4 "~/spark/sbin/start-slave.sh" -c 4 -m 3500M spark://vm1:7077

stop-spark:
	./run vm1 "~/spark/sbin/stop-master.sh"

	./run vm2 "~/spark/sbin/stop-slave.sh"
	./run vm3 "~/spark/sbin/stop-slave.sh"
	./run vm4 "~/spark/sbin/stop-slave.sh"

# Our pyspark is configured to launch jupyter (via environment variables and config files etc.)
start-pyspark:
	./run vm1 "~/spark/bin/pyspark" --master spark://vm1:7077 --deploy-mode client --executor-cores 4 --executor-memory 3500M --driver-memory 6G --conf spark.driver.maxResultSize=3G

stop-pyspark:
	./run vm1 pkill jupyter
	./run vm1 pkill pyspark

sync-spark-config:
	scp spark/* "vm1:~/spark/conf"
	scp spark/* "vm2:~/spark/conf"
	scp spark/* "vm3:~/spark/conf"
	scp spark/* "vm4:~/spark/conf"


restart-all: stop-all
	./run-all sudo shutdown -r now


hdfs-du:
	./run-all du -h -d0 "~/hdfs"

hdfs-report:
	./run vm1 hdfs dfsadmin -report

#

mount-src-harish:
	@#./run vm1 mkdir -p "~/github-analytics/src-harish"
	@echo sshfs hthuwal@$(MY_IP):/home/hthuwal/IITD/COP701/github-analytics/src /home/vm1/github-analytics/src-harish

mount-src-zafar:
	@#./run vm1 mkdir -p "~/github-analytics/src-zafar"
	@echo sshfs dufferzafar@$(MY_IP):/home/dufferzafar/dev/github-analytics/src /home/vm1/github-analytics/src-zafar
