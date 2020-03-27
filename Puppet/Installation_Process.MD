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
    
  - Install the Puppet Master by using yum.
  
    `yum install puppetserver.noarch -y`
    
  - Start the PuppetServer
  
    `systemctl start puppetserver`
    
  - Set the SoftLink
  
    `ln -s /opt/puppetlabs/bin/puppet /usr/bin/puppet`
    
## Puppet-Slave installation


  - Download the required packager from https://yum.puppet.com/. I am using PUPPET5.
  
    `rpm -Uvh https://yum.puppet.com/puppet5/puppet5-release-el-7.noarch.rpm`
    
  - Install Puppet Slave/Agent.
  
    `yum install puppet-agent -y`
    
  - Check the Puppet Status
  
    `systemctl status puppet`
    
  - Set the SoftLink
  
    `ln -s /opt/puppetlabs/bin/puppet /usr/bin/puppet`
    
## Master-Agent Configaration

  - Edit the "/etc/puppetlabs/puppet/puppet.conf" file in all the Agents and add the below info:
  
        [main]
        certname = puppetslave.cisco.com
        server = puppetmaster.cisco.com

  - Run the follow commands to verify the pending cert requests.
  
    `puppet cert list`
    
  - To see all the pending and connected connections.
  
    `puppet cert list --all`
    
    O/P: 
    
          [root@puppetmaster ~]# puppet cert list --all
            2020-03-27 11:24:53.979090 WARN  puppetlabs.facter - locale environment variables were bad; continuing with LANG=C LC_ALL=C
            Warning: `puppet cert` is deprecated and will be removed in a future release.
               (location: /opt/puppetlabs/puppet/lib/ruby/vendor_ruby/puppet/application.rb:370:in `run')
              "puppetslave.cisco.com"  (SHA256) 1A:95:3A:EE:77:2F:88:AD:05:D3:57:5D:4C:50:4B:E9:AA:CF:05:D1:37:42:51:A1:41:43:4E:4C:70:83:29:A8
            + "puppetmaster.cisco.com" (SHA256) E9:3B:47:40:59:1D:E4:FB:49:7B:D4:A8:D7:A2:32:30:05:44:C1:6D:EB:20:F8:74:DB:E3:71:68:B1:4E:05:EF (alt names: "DNS:puppet", "DNS:puppetmaster.cisco.com") **
    
  - Sign a certificate from pending requests like below.
  
    `puppet cert sign puppetslave.cisco.com`
   
