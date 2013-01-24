#!/bin/bash

#Not sure if needed
REPO=./
#USER DEFINED
NUM_REPS=1

for TASK in seq 1 $NUM_REPS ; do
echo $TASK
#Create an AWS volume
#    ec2-create-volume --size 20 --zone us-west-2a

#Grabs the Volume number that was created most recently
#    VOL_NUMBER=$(ec2-describe-volumes | tail -n2 | tr "|" "\n" | head -n2 | tail -n1 | tr -d ' ')

#Start up an amazon instance. Will have to change if running own
#Debian instance
    ec2-run-instance ami-20800c10 -k amazon_key -g ssh_allowed --instance-type t1.micro --wait=10

    sleep 60
#Pause time to let instance start up
    instance=$(ec2-describe-instances | tr '\t' '\n' | tail -n 4 | head -n1)
    dns=$(ec2-describe-instances | tr '\t' '\n' | tail -n 2 | head -n1)

#    ec2-attach-volume ${VOL_NUMBER} -i ${instance} -d /dev/sdf
#THIS WORKS
    cat ./scripts/inner_run.sh | ssh -i ~/.ssh/amazon_key -o StrictHostKeyChecking=no ubuntu@${dns} /bin/bash
     
#    ./scripts/setup_script.sh

#    python run_config.py --parameters ./parameters.cfg --seed ${TASK} &

done
