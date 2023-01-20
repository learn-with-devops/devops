Zabbix Installation On RedHat/CentOS 8: 
---------------------------------------

1. Disable SELinux


    sudo setenforce 0
    sudo sed -i 's/^SELINUX=.*/SELINUX=permissive/g' /etc/selinux/config
    cat /etc/selinux/config | grep SELINUX=


2. Install Apache


    dnf -y install @httpd
    systemctl enable --now httpd


3. Install MariaDB


    dnf module install mariadb
    rpm -qi mariadb-server (To know version of MariaDB)
    systemctl enable --now mariadb
    mysql_secure_installation  (Harden your database)
    mysql -u root -p


4. Create Database & User


    CREATE DATABASE zabbix character set utf8 collate utf8_bin;
    GRANT ALL PRIVILEGES ON zabbix.* TO zabbix@'localhost' IDENTIFIED BY 'password';
    FLUSH PRIVILEGES;
    QUIT;


5. Zabbix Server Frontend Installation


    dnf -y install https://repo.zabbix.com/zabbix/5.0/rhel/8/x86_64/zabbix-release-5.0-1.el8.noarch.rpm
    dnf -y install zabbix-server-mysql zabbix-web-mysql zabbix-apache-conf zabbix-agent


6. Import Initial Schema


    zcat /usr/share/doc/zabbix-server-mysql*/create.sql.gz | mysql -u zabbix -p zabbix


7. Configure Zabbix Server Conf ( /etc/zabbix/zabbix_server.conf )


    DBName=zabbix
    DBUser=zabbix
    DBPassword=StrongPassword

8. Configure PHP for Zabbix Frontend


    vi /etc/php-fpm.d/zabbix.conf
    php_value[date.timezone] = Asia/Kolkata


9. Restart Zabbix services


    systemctl restart zabbix-server zabbix-agent httpd php-fpm
    systemctl enable zabbix-server zabbix-agent httpd php-fpm

    systemctl status zabbix-server  ( Server Status )


10. Configure Zabbix Frontend Optional


    vi /etc/php.ini
    memory_limit 128M
    upload_max_filesize 8M
    post_max_size 16M
    max_execution_time 300
    max_input_time 300


11. Restart the Apache and PHP 

    sudo systemctl restart httpd php-fpm



Agent Installation : 
--------------------

1. Install agent on remote server 


    yum install https://repo.zabbix.com/zabbix/5.0/rhel/8/x86_64/zabbix-release-5.0-1.el8.noarch.rpm


2. yum install zabbix-agent -y

3. Configure Zabbix Agent


    vi /etc/zabbix/zabbix_agentd.conf
    Server=10.5.5.1
    ServerActive=10.5.5.1
    Hostname=client

4. Restart Zabbix agent


    systemctl restart zabbix-agent
    

<img width="1152" alt="Screenshot 2022-07-16 at 11 53 33 PM" src="https://user-images.githubusercontent.com/51190838/179367531-a484eb10-361d-4fa9-883e-a93d67050a8b.png">

