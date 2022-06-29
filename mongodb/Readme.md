# Mongo DB Installation On RedHat/ CentOs 8

## Enable MongoDB 4.4 Yum Repository

    $ sudo vi /etc/yum.repos.d/mongodb-org-4.repo

    [mongodb-org-4.4]
    name=MongoDB Repository
    baseurl=https://repo.mongodb.org/yum/redhat/$releasever/mongodb-org/4.4/x86_64/
    gpgcheck=1
    enabled=1
    gpgkey=https://www.mongodb.org/static/pgp/server-4.4.asc
    
## Install MongoDB package with dnf / yum command

    $ sudo yum install -y mongodb-org
    
    
    
## Allow authentication in /etc/mongod.conf file and then Set User, Password 

    security:
      authorization: enabled
      
    UserName and Password : 
    > use admin
    > db.createUser( { user: "admin", pwd: "admin", roles: [ { role: "userAdminAnyDatabase", db: "admin" }, "readWriteAnyDatabase" ] } )
  
## Allow remote access by modifing /etc/mongod.conf

    net:
      port: 27017
      bindIp: 127.0.0.1,10.240.128.15 



    
## Start and Enable the MongoDB Service

    $ getenforce
    Enforcing
    $ sudo setenforce 0
    $ sudo sed -i s/^SELINUX=.*$/SELINUX=permissive/ /etc/selinux/config


    $ sudo systemctl start mongod
    $ sudo systemctl enable mongod
    $ sudo systemctl status mongod
    
  
## Access the MongoDB from Compass 
<img width="780" alt="Screenshot 2022-06-29 at 11 47 25 PM" src="https://user-images.githubusercontent.com/51190838/176507682-436fe577-a317-4186-91e0-93b988f06c1f.png">
