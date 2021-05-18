##  Docker Image commands

	- List out the Docker Images.

	  	docker images
	  	docker image ls

	- History of the image 

		docker image history 5ea11339b1c3 <image Id>

	- TO know the complete info of the Image

	    docker image inspect <image Id>

	- Download any image from Docker Hub

	    docker pull <image-Name >

	- Upload an image to docke Hub

		docker push <image-Name >

	- Remove an image 

	    docker rmi <image Id>

	- Create a Tag for the Image

		docker tag be1f31be9a87 creack/nginx:latest1.0
    
    - Build an image

        docker build -t <image-name > .
        docker build --tag <image-name > <Dockerfile_location>
	
    - Remove Unwanted Images
    
        docker image prune
	
    - Create a Image Out of container

    	docker commit [OPTIONS] CONTAINER [REPOSITORY[:TAG]]
 
