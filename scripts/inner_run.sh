#!/bin/bash

sudo mkdir -p /mnt/ebs 
sudo mkfs -t ext4 /dev/xvda1
sudo mount /dev/xvda1 /mnt/ebs

sudo apt-get -y -q install git > /dev/null
sudo apt-get -y -q install python2.7-dev > /dev/null
sudo apt-get -y -q install build-essential > /dev/null
sudo apt-get -y -q install python-pip > /dev/null
git clone git://github.com/nahumj/structure_and_landscapes.git
cd structure_and_landscapes
./configure
make
sudo make install 

#python run scripts

#ping the central server

#scp data back