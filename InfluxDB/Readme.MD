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
