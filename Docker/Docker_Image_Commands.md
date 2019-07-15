 Docker Container commands

	- Check what are processes are running on top of container

	    docker top <container id>

	- Remove all stopped containers

	    docker container prune

	- List the ports are listing

	    docker port <container>

	- To check running Docker containers

	  	docker container ps

	- To check running and stopped docker containers

	  	docker container ps -a

	- To stop/start/restart/remove the docker container

	  	docker stop/start/restart/rm < container_id > 

	- Remove the docker running container forcefully

	    docker rm -f <container id >       ----  -f = forcefully

	- Crerate a docker container from docker Image in background

	    docker container run -t -d --name <name> <image id>

	    -t --> Allocate a terminal
	    -i --> Intaractive mode (-i (interactive) flag to keep stdin open)
	    --read-only  (Set the container to be read-only)

	- Create a container with a port

	    docker run -it -d -p 8000:80 --name <name> <image id>

	- Create a container from forground with port

	    docker container run  -i -t -p 8003:80  --name nginx-7 be1f31be9a87 bash

	- Check the Logs of container

	    docker logs < container_id >

	- pause/Unpass the processes running inside the container.

	    docker pause/unpause 936b4f0f8c6b

	- see the processes that are running inside the docker containe

	    docker top <container_id >

	- Display a live stream of container(s) resource usage statistics

	    docker stats

	- Rename the docker container

	    docker rename <CONTAINER>  <NEW_NAME>

	- Create a new image from a container's changes

	    docker commit < container_Id > <new_Image name>

	- Copy the files from local to container

	    docker cp <source_path > <container_id >:/root/anand/

	- Test the ping command while running a container

	    docker exec -it my_container ping -w3 google.com
