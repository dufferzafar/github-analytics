
## Cluster

### 20/10/2017

* Change password to: `G1thu8`

* Setup Passwordless SSH:

`ssh-copy-id -i ~/.ssh/id_rsa.pub vm*`

* Update/Upgrade

`sudo apt up{date, grade}`

* Installed Java

`sudo apt install openjdk-8-{jre,jdk}`

* Appended hosts information on all machines

`vim /etc/hosts`

* Passwordless from each VM to another

`./run-all ssh-keygen`

`./run-all ssh-copy-id -i /home/baadalvm/.ssh/id_rsa.pub vm*`

* Ranger!

`./run-all sudo apt install ranger`

* Symlink environment details

`./run-all ln -sf "/home/baadalvm/github-analytics/cluster-setup/.bash_profile" "/home/baadalvm/.bash_profile"`

### 23/10/2017

* Change password of all root accounts to `G1thu8`

`sudo passwd root`

* Rename all `baadalvm` users to `vm*`
(because hadoop log files are named after users so all should be different)

```
ssh root@vm*

skill -KILL -u baadalvm
sudo usermod -l vm* baadalvm
usermod -d /home/vm* -m vm*

ssh vm*@vm*
```

* Correct path in the hdfs-site.xml file

`./run vm* sed -i "s/baadalvm/vm*/" ~/hadoop/etc/hadoop/hdfs-site.xml`

* Re-link the `.bash_profile`

`./run vm* ln -sf "/home/vm*/github-analytics/cluster-setup/.bash_profile" "~/.bash_profile"`

* Add `~/.ssh/config` to all machines
(because of an issue similar to: https://stackoverflow.com/questions/28658276/)

`scp ssh-config "vm*:~/.ssh/config"`

* Change the hostname of all machines
(because the log file issue is still present :/)

```
sudo hostname vm* 
sudo vim /etc/hostname # change hostname
sudo vim /etc/hosts # comment the 127.0.1.1 line
```

We finally have all nodes on the UI! yay!

In hindsight, we shouldn't have changed the usernames! (should we change them back :P)

* Also got Yarn to work by providing a config having minimum RAM value.

### 6/11/2017

* Changed Yarn's RAM value to 3.5GB 

* Installed Spark on all machines

# Master

* scp hadoop tarball to master
* untar
* overwrite with our config files

# Todo

* hadoop config files?!
