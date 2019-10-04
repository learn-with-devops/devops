#!/bin/sh

###############################################################
#Purpose      :  Ansible Install on RedHat Linux
#Version      :  0.1
#Author       :  Anand Reddy
#Created      :  29/12/18
###############################################################

#sudo su -

echo "################################################################"
echo "############# Ansible Installation Started  ####################"
echo "################################################################"

yum update -y

yum install wget git unzip zip python php java-1.8.0-openjdk-devel -y

wget https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm

rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm

yum -y install ansible
