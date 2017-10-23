push-setup:
	rsync -r . vm1:/home/vm1/github-analytics/cluster-setup/
	rsync -r . vm2:/home/vm2/github-analytics/cluster-setup/
	rsync -r . vm3:/home/vm3/github-analytics/cluster-setup/
	rsync -r . vm4:/home/vm4/github-analytics/cluster-setup/

copy-hadoop-config:
	ssh -t vm1 cp /home/vm1/github-analytics/cluster-setup/hadoop/* /home/vm1/hadoop/etc/hadoop/

start-dfs:
	./run vm1 "~/hadoop/sbin/hadoop-daemon.sh" start namenode

	./run vm2 "~/hadoop/sbin/hadoop-daemon.sh" start datanode
	./run vm3 "~/hadoop/sbin/hadoop-daemon.sh" start datanode
	./run vm4 "~/hadoop/sbin/hadoop-daemon.sh" start datanode

stop-dfs:
	./run vm1 "~/hadoop/sbin/hadoop-daemon.sh" stop namenode

	./run vm2 "~/hadoop/sbin/hadoop-daemon.sh" stop datanode
	./run vm3 "~/hadoop/sbin/hadoop-daemon.sh" stop datanode
	./run vm4 "~/hadoop/sbin/hadoop-daemon.sh" stop datanode

restart-all:
	./run-all sudo shutdown -r now

hdfs-usage:
	./run-all du -h -d0 "~/hdfs"
