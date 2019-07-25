Official Website: https://www.nagios.org/

Steps for Installing and Configuring Nagios on Centos 7

Installing Dependencies

#yum install -y httpd php wget unzip

Adding Libraries

#yum install -y gcc glibc glibc-common make gd gd-devel net-snmp

You will have to add the nagios user to the 
system so you avoid running it as root:

# useradd nagios

And a new nagcmd group that will allow external 
commands to be run via the web interface:

# groupadd nagcmd
# usermod -G nagcmd nagios
# usermod -G nagcmd apache

Next step is to download the installation packages. 
Create a new directory to store the downloaded 
content:

# mkdir ~/nagios
# cd ~/nagios

You can use wget to download the files:

# curl -L -O https://assets.nagios.com/downloads/nagioscore/releases/nagios-4.1.1.tar.gz
# curl -L -O http://nagios-plugins.org/download/nagios-plugins-2.1.1.tar.gz

Extract the files with Tar:

# tar zxvf nagios-4.0.7.tar.gz
# tar zxvf nagios-plugins-2.0.3.tar.gz

Now we need to compile and install the files so 
we go to the Nagios directory and 
run the configuration script

# cd nagios-4.0.7
# ./configure --with-command-group=nagcmd

Next we need to compile and install the Nagios files:

# make all
# make install

Finally we need to install the init scripts, 
the required files to run Nagios from the command 
line and the sample configuration files 
with the following commands:

# make install-init
# make install-commandmode
# make install-config

Now that we have Nagios installed and ready to 
run we need to install the web component 
by running the following command:

# make install-webconf

And we need to setup the password for the 
user nagiosadmin. 

# htpasswd -s -c /usr/local/nagios/etc/htpasswd.users nagiosadmin

Restart apache for the settings to take effect:

# systemctl start httpd.service

It’s time to install the Nagios Plugins by 
running the following commands:

# cd ~/nagios/nagios-plugins-2.0.3
# ./configure --with-nagios-user=nagios --with-nagios-group=nagios
# make
# make install

Next we have to make Nagios start at boot time, 

# /usr/local/nagios/bin/nagios -v /usr/local/nagios/etc/nagios.cfg

If everything is fine add the service to run on boot with this commands:

# chkconfig --add nagios
# chkconfig --level 35 nagios on

And start the service with the following command:

# systemctl start nagios.service

Open Web Browser:

http://Ip-Adddress/nagios

Username: nagiosadmin
password: As Set above
