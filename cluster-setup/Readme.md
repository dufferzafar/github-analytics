
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

# Master

``

# Todo

* wake up vm1

* scp hadoop on master

* hadoop config files?!
