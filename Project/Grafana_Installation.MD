## Grafana Installation :

#### 1. Install Grafana using the installation instructions: 

	$ wget https://grafanarel.s3.amazonaws.com/builds/grafana_3.0.4-1464167696_amd64.deb
	$ sudo apt-get install -y adduser libfontconfig
	$ sudo dpkg -i grafana_3.0.4-1464167696_amd64.deb


#### 2. Start the server and automatically start the server on boot up
	
	- sudo service grafana-server start
	- sudo systemctl enable grafana-server.service
	
#### 3. Test

        - In your browser, go to localhost:3000
        - Log in as (user) admin, (password) admin
