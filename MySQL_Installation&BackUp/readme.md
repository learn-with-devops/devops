## MySQL 8 Installation

Note: 

        refer the below document for MySql Installation
        Ref : https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-centos-7
        
        
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


## Interview Questions



# Create a Table with CITY
CREATE table city(
	cid INT NOT NULL AUTO_INCREMENT,
	city_name VARCHAR(100) NOT NULL,
	PRIMARY KEY(cid)
)

# Insert data to City Table
INSERT INTO city(city_name) values ('Chennai'),
('Bangalore'),
('Ahammadabad'),
('Delhi'),
('Mumbai'),
('Hyderabad');

# Create a table for customer
CREATE TABLE customer(
id INT NOT NULL,
first_name VARCHAR(40) NOT NULL,
lastname VARCHAR(30) NOT NULL, 
city INT NOT NULL,
PRIMARY KEY(id),
FOREIGN KEY(city) REFERENCES city(cid)
);

# Insert table into customer
INSERT INTO customer(id, first_name, lastname, city) values (571, "Anand", "Reddy", 5),
(572, "Kusuma", "N", 2),
(576, "Balaji", "Naidu", 6),
(589, "Vijay", "Prakash", 4),
(596, "ANanth", "Babu", 2);

# Insert additional data
INSERT INTO customer (id, first_name, lastname, city) values (899, "Anand", "Rathod", 1);

select * from city;
select * from customer;


# Join both tables 
select id, first_name, lastname, city_name as city from customer c JOIN city ci WHERE c.city = ci.cid;

# Count Number of Rows in a Table
select COUNT(*) from customer;

# Filter Condition
select * from customer where first_name = "ANANd";

# List out the items based on Desc order
select * from customer ORDER BY first_name DESC;

# Coloum 1 inn ASC order and coloumn 2 in DESC oder.
select * from customer ORDER BY lastname ASC, city DESC;

# List out unique values
select DISTINCT first_name from customer;

# AND | OR | IN keyword
select * from customer WHERE first_name = "Anand" AND city = 1;
select * from customer WHERE first_name = "Anand" OR city = 1;
select * from customer WHERE city IN (1,4,6);

# IS NULL 
select * from customer WHERE first_name IS NULL;

# Conact and coloumn alias
select CONCAT(first_name,' ',lastname) as Full_Name from customer;

