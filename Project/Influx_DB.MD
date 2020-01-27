## Influx DB Installation

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
