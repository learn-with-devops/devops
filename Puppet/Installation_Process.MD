# Puppet Installation

## Puppet-Master Pre-Reqisites Setup

  - Launch a CENTSOS Server in AWS console with min 4GB RAM and 2CORE CPU.
  
    Allow the following ports : 22, ALL TCP , All ICMP , 8140.
  
  - Edit the /etc/hosts file and add the master and slave names here and do the same in slave servers also.
  
    Ex: 
    
        127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
        ::1         localhost localhost.localdomain localhost6 localhost6.localdomain6
        172.31.30.44 puppetslave.cisco.com
        172.31.10.128 puppetmaster.cisco.com puppetmaster puppet
     
    Note : 
    
     Do the PING test to check like 
    
    `ping puppetslave.cisco.com`
    
        
  - Ser the Hostname for the Master and Slave Servers.
  
      `hostnamectl set-hostname puppetmaster.cisco.com`
      
      `bash`

## Puppet-Master Installation Steps

  - Download the required packager from https://yum.puppet.com/. I am using PUPPET5.
  
    `rpm -Uvh https://yum.puppet.com/puppet5/puppet5-release-el-7.noarch.rpm`
    
  - Install the Puppet by using yum.
  
    `yum install puppetserver.noarch -y`
    
  - Start the PuppetServer
  
    `systemctl start puppetserver`
    
  
## Puppet-Slave installation


   
