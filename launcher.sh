#!/bin/bash

#Not sure if needed
REPO=./

#Create an AWS volume
ec2-create-volume --size 20 --zone us-west-2b

#Grabs the Volume number that was created most recently
VOL_NUMBER=$(ec2-describe-volumes | tail -n2 | tr "|" "\n" | head -n2 | tail -n1 | tr -d ' ')

#Start up an amazon instance. Will have to change if running own
#Debian instance
ec2-run-instance ami-fcf27fcc -k amazon_key -g ssh_allowed --instance-type t1.micro --wait=10

#Pause time to let instance start up
sleep 10

instance=$(ec2-describe-instances | tr '\t' '\n' | tail -n 4 | head -n1)
dns=$(ec2-describe-instances | tr '\t' '\n' | tail -n2 | head -n1)

ec2-attach-volume ${VOL_NUMBER} -i ${instance} -d /dev/sdf

ssh -i ~/.ssh/amazon_key ${dns}

echo yes

sleep 5

#sudo mkdir -p /mnt/ebs && sudo mkfs -t ext4 /dev/xvdf && sudo /dev/xvdf /mnt/ebs

#sudo apt-get -y install git

#git clone git://github.com/nahumj/structure_and_landscapes.git
