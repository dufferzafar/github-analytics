
# Cluster Setup

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

`./run-all ssh-copy-id -i /home/baadalvm/.ssh/id_rsa.pub vm{1,2,3,4}`

* Ranger!

`./run-all sudo apt install ranger`

* Symlink environment details

`./run-all ln -sf "/home/baadalvm/github-analytics/cluster-setup/.bash_profile" "/home/baadalvm/.bash_profile"`

# Master

* scp hadoop tarball to master
* untar
* overwrite with our config files

# Todo

* hadoop config files?!
