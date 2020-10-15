## MySQL 8 Installation

- Setup Yum repository

        rpm -Uvh https://repo.mysql.com/mysql80-community-release-el7-3.noarch.rpm
        
- Install MySQL 8 Community Server
        
        sed -i 's/enabled=1/enabled=0/' /etc/yum.repos.d/mysql-community.repo

-  execute the following command to install MySQL 8
        
        yum --enablerepo=mysql80-community install mysql-community-server

- Start MySQL server
        
        service mysqld start

- Show the default password for root user

        grep "A temporary password" /var/log/mysqld.log
        
- MySQL Secure Installation

        mysql_secure_installation
        
- Restart and enable the MySQL service

        service mysqld restart
        
- autostart mysql service on system’s startup

        chkconfig mysqld on
        
- Connect to MySQL
        
        mysql -u root -p

