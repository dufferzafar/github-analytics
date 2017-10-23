push-setup:
	rsync -r . vm1:/home/vm1/github-analytics/cluster-setup/
	rsync -r . vm2:/home/vm2/github-analytics/cluster-setup/
	rsync -r . vm3:/home/vm3/github-analytics/cluster-setup/
	rsync -r . vm4:/home/vm4/github-analytics/cluster-setup/

copy-hadoop-config:
	ssh -t vm1 cp /home/vm1/github-analytics/cluster-setup/hadoop/* /home/vm1/hadoop/etc/hadoop/

