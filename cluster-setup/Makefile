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

start-yarn:
	./run vm1 "~/hadoop/sbin/yarn-daemon.sh" start resourcemanager

	./run vm2 "~/hadoop/sbin/yarn-daemon.sh" start nodemanager
	./run vm3 "~/hadoop/sbin/yarn-daemon.sh" start nodemanager
	./run vm4 "~/hadoop/sbin/yarn-daemon.sh" start nodemanager

stop-yarn:
	./run vm1 "~/hadoop/sbin/yarn-daemon.sh" stop resourcemanager

	./run vm2 "~/hadoop/sbin/yarn-daemon.sh" stop nodemanager
	./run vm3 "~/hadoop/sbin/yarn-daemon.sh" stop nodemanager
	./run vm4 "~/hadoop/sbin/yarn-daemon.sh" stop nodemanager

sync-yarn-config:
	scp hadoop/yarn-site.xml "vm1:~/hadoop/etc/hadoop/yarn-site.xml"
	scp hadoop/yarn-site.xml "vm2:~/hadoop/etc/hadoop/yarn-site.xml"
	scp hadoop/yarn-site.xml "vm3:~/hadoop/etc/hadoop/yarn-site.xml"
	scp hadoop/yarn-site.xml "vm4:~/hadoop/etc/hadoop/yarn-site.xml"

restart-all:
	./run-all sudo shutdown -r now

hdfs-du:
	./run-all du -h -d0 "~/hdfs"

hdfs-report:
	./run vm1 hdfs dfsadmin -report
