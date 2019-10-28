Docker Swarm :
--------------

Initial Setup Process 

	- Create 3 CentOS servers and make 1 server as Master and 2 as Slave/Worker nodes

    - Open the following ports on all servers.
	
	  # Ports
	     - 80
		 - 4789 ( For Overlay Network )
		 - 2377 ( For Cluster Management like heart-beat info , node health check )
		 - 7946 ( Nodes can communicate each other )
		 
	- Install Docker on 3 servers.
	
	- Now Jump into the Master Node and run the following commands
	
	  # Initialize the Docker Swarm Mode
	  docker swarm init

	- Once u run the above command on master then you will get Docker-Swarm-join-Token. Plese copy the entire line and run that into the slave nodes. That's it.

	  Ex: docker swarm join --token SWMTKN-1-53lc6spjk0no0dn3kc4s3zlgx5xuszdvdddw1uy1mirlerkimf-1jjymklcjt5lo660pm7hd8t29 192.168.65.3:2377

    - If you want to verify the cluster list.
   
      docker node ls

    
    Other Commands:
    ---------------
    
    - Make Worker node as Master

		docker node update --role manager ip-172-31-89-219.ec2.internal
		
	- Make Master node as Worker Node
	
		docker node update --role worker ip-172-31-89-219.ec2.internal
		
	- If you last the Docker Join Token
	
		docker swarm init --advertise-addr 54.158.48.156
		
	- If u want to leave from the Swarm
	
	    docker swarm leave
		
    - If you forgot the Joining token then use this to get
	
		docker swarm join-token manager
		
	
	

Docker Swarm Container Deployment types :

	1 . Service Deployment  
	2 . Stack Deployment 
	
	
	Service Deployment :
	--------------------
	
	# Deploy a Service and create 5 replicas
	docker service create --name httpd-test --replicas 5 -p 8080:80 nginx
	
	# List Out the Services
	docker service ls
	
	# Want to check in which slave our container running
	docker service ps <service-name>
	
	# If you want to remove service 
	docker service rm <service-name>
	
	# Inspect the service
	docker service inspect <service name>
	docker service inspect <service name> --pretty
	
	# Scale Up/Down the Container
	docker service update --replicas 10 <Service Name>
	docker service scale <Service Name > =12
	
	
	Stack Deployment:
	--------------------

    # Docker Stack Deployment with docker-compose file
    docker stack deploy -c docker-compose.yml anna

    # List out the stacks 
    docker stack ls

    # List out the containers where it is running
    docker stack ps <stack name >

    # remove the stack
    docker stack rm <stack name>

    # Docker-stack service list
    docker stack services anna

    # to check the logs of Stack
    docker service logs rotem_app

    Note:  for Logs check keep this things need to follow 
    vi /etc/docker/daemon.json
		> add follow
		  {"experimental":true}
		  
	and finally restart the docker
		sudo systemctl restart docker
		
     # Onother way to check the logs 
     docker logs $(docker inspect --format "{{.Status.ContainerStatus.ContainerID}}" pioi4lfw9iq8)
	
     # Example-1 :
	 
	version: "3"

	services:
	   app:
		  image: httpd
		  deploy:
			replicas: 5
			resources:
			  limits:
				cpus: "0.2"
				memory: 50M
			restart_policy:
			  condition: on-failure
		  ports:
			- "80:80"
		  networks:
			- my-httpd

	networks:
	  my-httpd:
	  
	  
    # Example-2
    
    version: '3'

	services:
	   db:
	     image: mysql:5.7
	     deploy:
	       replicas: 4
	       restart_policy:
		 condition: on-failure
	     volumes:
	       - db_data:/var/lib/mysql
	     restart: always
	     environment:
	       MYSQL_ROOT_PASSWORD: somewordpress
	       MYSQL_DATABASE: wordpress
	       MYSQL_USER: wordpress
	       MYSQL_PASSWORD: wordpress
	     networks:
	       - wordpress-overlay

	   wordpress:
	     depends_on:
	       - db
	     image: wordpress:latest
	     deploy:
	       replicas: 2
	       restart_policy:
		 condition: on-failure
	     ports:
	       - "8000:80"
	     restart: always
	     networks:
	       - wordpress-overlay
	     environment:
	       WORDPRESS_DB_HOST: db:3306
	       WORDPRESS_DB_USER: wordpress
	       WORDPRESS_DB_PASSWORD: wordpress
	volumes:
	    db_data:
	networks:
	    wordpress-overlay:

----------------------------------------------------
version: '3'
services:
    web:
       image: httpd:latest
       deploy:
          replicas: 4
          restart_policy:
               condition: on-failure
       ports:
          - "80:80"
	  
