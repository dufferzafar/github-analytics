default: copy-hadoop-config

push-setup:
	rsync -r . vm1:/home/baadalvm/github-analytics/cluster-setup/
	rsync -r . vm2:/home/baadalvm/github-analytics/cluster-setup/
	rsync -r . vm3:/home/baadalvm/github-analytics/cluster-setup/
	rsync -r . vm4:/home/baadalvm/github-analytics/cluster-setup/

copy-hadoop-config: push-setup
	ssh -t vm1 cp /home/baadalvm/github-analytics/cluster-setup/hadoop/* /home/baadalvm/hadoop/etc/hadoop/
