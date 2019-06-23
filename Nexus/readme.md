# Nexus

### [Nexus Installation Process](https://github.com/learn-with-devops/devops/blob/master/Nexus/Nexus_Installation.md)

### Docker Image Pulling and pushing to Nexus repo

      # Please Pull one basic/required image to your server
      docker pull alpine

      Note : 

      # If you want download an Image from Nexus DTR directly then follow like below
      docker pull <nexus-hostname>:<repository-port>/<image>

      # Rename the tag for that image
      docker tag alpine <nexus-server-ip>:<repo-port>/<imag_name>
      ex: 
      docker tag alpine 18.216.203.67:8088/alpine:latest

      # Finally push your image to Docker registory
      docker push <image_name>

  
