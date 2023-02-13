# SonarQube Installation on RedHat 8.6 Server

### Prerequisites

1. Update the OS and Install pre-required softwares
```sh
   sudo yum update -y
   sudo yum install vim wget curl unzip git java-11-openjdk-devel -y
```

2. Configure SELinux as Permissive
```sh
sudo setenforce 0
sudo sed -i 's/^SELINUX=enforcing$/SELINUX=permissive/' /etc/selinux/config
```

3. Set File limit, add below content in  "/etc/sysctl.conf"

- sudo vim /etc/sysctl.conf 

```sh
vm.max_map_count=262144
fs.file-max=65536
```

- Then reload sysctl configuration as follows:

```sh
   sudo sysctl --system
```

- Replace "1" with "0" in the string "localpkg_gpgcheck" from this file 'vi /etc/dnf/dnf.conf'

```sh
localpkg_gpgcheck=0
```

4. Create a user for SonarQube

```sh
useradd sonar
passwd sonar
```


### PostGress DB Installation

Install Postgres 

 ```sh
      sudo dnf -y update
      sudo dnf -y install https://download.postgresql.org/pub/repos/yum/reporpms/EL-8-x86_64/pgdg-redhat-repo-latest.noarch.rpm
      sudo dnf -qy module disable postgresql
      sudo dnf -y install postgresql13 postgresql13-server
      sudo /usr/pgsql-13/bin/postgresql-13-setup initdb
      sudo systemctl enable --now postgresql-13
      systemctl status postgresql-13
 ```

Create db and user for Sonarqube:
```sh
     sudo su - postgres 
     psql

     Run Below: 
     
     create user sonar;
     create database sonar_db owner sonar;
     grant all privileges on database sonar_db to sonar;
     ALTER USER sonar WITH ENCRYPTED password 'sonar';
     exit
     exit
```

SonarQube 9.0 Installation :

```sh
   cd /opt/
   sudo wget https://binaries.sonarsource.com/Distribution/sonarqube/sonarqube-9.1.0.47736.zip
   unzip sonarqube-9.1.0.47736.zip
   mv sonarqube-9.1.0.47736 sonarqube
   sudo chown -R sonar:sonar /opt/sonarqube
```


configuration changes on "vim /opt/sonarqube/conf/sonar.properties" file : 

```
##Database details
sonar.jdbc.username=sonar
sonar.jdbc.password=StrongPassword
sonar.jdbc.url=jdbc:postgresql://localhost/sonar_db

##How you will access SonarQube Web UI
sonar.web.host=0.0.0.0
sonar.web.port=9000

##Java options
sonar.web.javaOpts=-Xmx512m -Xms128m -XX:+HeapDumpOnOutOfMemoryError
sonar.search.javaOpts=-Xmx512m -Xms512m -XX:MaxDirectMemorySize=256m -XX:+HeapDumpOnOutOfMemoryError

##Also uncomment the following Elasticsearch storage paths
sonar.path.data=data
sonar.path.temp=temp
```


Add SonarQube SystemD service file "vim /etc/systemd/system/sonarqube.service"

```
[Unit]
Description=SonarQube service
After=syslog.target network.target

[Service]
Type=forking
ExecStart=/opt/sonarqube/bin/linux-x86-64/sonar.sh start
ExecStop=/opt/sonarqube/bin/linux-x86-64/sonar.sh stop
LimitNOFILE=65536
LimitNPROC=4096
User=sonar
Group=sonar
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

Enable and Start the SonarQube Service

```
sudo systemctl daemon-reload
sudo systemctl start sonarqube.service
sudo systemctl enable sonarqube.service
sudo systemctl status sonarqube.service
```

SonarQube application uses port 9000. access SonarQube from browser
```sh
  http://<PUBLIC_IP>:9000
  
  Default Username and Password :  admin & admin
```

references: 
----------

- Application setup on SonarQube : https://www.youtube.com/watch?v=-5YKWZhkf6g&ab_channel=ValaxyTechnologies
- Reference Link : https://www.fosstechnix.com/how-to-install-sonarqube-on-centos-8/




