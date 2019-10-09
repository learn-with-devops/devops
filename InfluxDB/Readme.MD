# InfluxDB

	Influxdata is a platform for storing, collecting, visualizing and managing time-series data. 
	It is faster than mysql. Currently Influxdb is the most famous time series database. 
	In influxdb time is the primary key. 
 

## Influx DB Installation on Ubuntu Server

#### Update the server

        - apt-get update
	- apt-get upgrade
	
#### Adding the influx package to apt repository

	curl -sL https://repos.influxdata.com/influxdb.key | sudo apt-key add -
	source /etc/lsb-release
	echo "deb https://repos.influxdata.com/${DISTRIB_ID,,} ${DISTRIB_CODENAME} stable" | sudo tee /etc/apt/sources.list.d/influxdb.list

#### Install the InfluxDB

	sudo apt-get update && sudo apt-get install influxdb
	
#### Start the Influx 

	sudo service influxdb start


## Commands to work with Influx DB

	- Create aDatabase
	  create database <databasename>
	  
	- List out the data bases
	  show databases
	  
	- Swtich to that Database
  	  use <database>
	  
	- Create a Measurment (table).
	  // Here measurements nothing but tables...No need to create a table structure..Directly we can create a table with specific coloumns.
	  
	  insert <tablename>, column1=value column2=value
	  ex: 
	  	insert rank,class=ssc score=99.8
		
        - Display the details of measurments(table)
	  select * from <measurements>
	  
	- Where condition
	  // if it is number then use like below
	  select * from table where time>=99
	  
	  // If it is string then use like below
	  select * from table where name='somename'
	  
	 - List out the tables/measurements
	   show measurements
	   
	 - If you want to select couple of fileds from a table then use like this
	   select class,score from rank
	  
