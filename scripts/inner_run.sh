#!/bin/bash
echo Test2 > test.txt
sudo mkdir -p /mnt/ebs && sudo mkfs -t ext4 /dev/xvdf && sudo mount /dev/xvdf /mnt/ebs

sudo apt-get -y install git

git clone git://github.com/nahumj/structure_and_landscapes.git

#run install 

#python run scripts

#ping the central server

#scp data back