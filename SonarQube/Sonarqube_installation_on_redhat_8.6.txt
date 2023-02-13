# SonarQube Installation

### Prerequisites
1. Update the OS and Install pre-required softwares
```sh
   yum update -y
   yum install java-1.8.0-openjdk unzip wget –y
```

### Installation

Install MySQL 

 ```sh
  sudo yum install wget unzip -y
  wget http://repo.mysql.com/mysql-community-release-el7-5.noarch.rpm
  sudo rpm -ivh mysql-community-release-el7-5.noarch.rpm
  yum update -y
  sudo yum install mysql-server
  sudo systemctl start mysqld
 ```

Create db and user for Sonarqube:
```sh
  mysql -u root
  CREATE DATABASE sonarqube_db;
  CREATE USER 'sonarqube_user'@'localhost' IDENTIFIED BY 'password';
  GRANT ALL PRIVILEGES ON sonarqube_db.* TO 'sonarqube_user'@'localhost' IDENTIFIED BY 'password';
  FLUSH PRIVILEGES;
  exit
```
Download & unzip SonarQube 6.0:
```sh
  wget https://binaries.sonarsource.com/Distribution/sonarqube/sonarqube-6.7.6.zip
  unzip sonarqube-6.7.6.zip
  mv sonarqube-6.7.6 /opt/sonarqube
```

Create a user for SonarQube:
```
 useradd sonarqube
 passwd sonarqube
 chown -R sonarqube:sonarqube /opt/sonarqube
```

Add Sonar Qube user details in below file: 
```sh
  vi /opt/sonarqube/bin/linux-x86-64/sonar.sh
  #add below line
  RUN_AS_USER=sonarqube
```

Configure sonarqube with MySQL database:
```sh
  vi /opt/sonarqube/conf/sonar.properties
  #add below lines
  sonar.jdbc.username=sonarqube_user
  sonar.jdbc.password=password
  sonar.jdbc.url=jdbc:mysql://localhost:3306/sonarqube_db?useUnicode=true&characterEncoding=utf8&rewriteBatchedStatements=true&useConfigs=maxPerformance
```

Start SonarQube:
```sh
/opt/sonarqube/bin/linux-x86-64/sonar.sh start
```

SonarQube application uses port 9000. access SonarQube from browser
```sh
  http://<EC2_PUBLIC_IP>:9000
  
  Default Username and Password :  admin & admin
```

To Understand the SonarQube UI and Project analysis, watch this video : 

video : https://www.youtube.com/watch?v=-5YKWZhkf6g&ab_channel=ValaxyTechnologies
Reference URL : https://www.decodingdevops.com/sonarqube-installation-on-centos-rhel/


