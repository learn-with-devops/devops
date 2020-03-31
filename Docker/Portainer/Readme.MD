# Portainer

Portainer is a lightweight management UI which allows you to easily manage your different Docker environments (Docker hosts or Swarm clusters). 
It is meant to be as simple to deploy as it is to use. It consists of a single container that can run on any Docker engine 
(can be deployed as Linux container or a Windows native container). Portainer allows you to manage your Docker containers, images, volumes, networks and more !


## Installation

- Install the Docker on the servers.

    `yum install docker -y`
    
- Start the Docker 

    `service enable docker`
   
    `service start docker`
    
- create a volume dedicated for Portainer's data storage

    `docker volume create portainer_data`
    
- use docker command to run Portainer container

    `docker run -d -p 9000:9000 --name portainer --restart always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer`
    
    
## Access the Portainer UI

- Login to the UI

    `http://ip:90000`
    
    `UserName : admin`
    `Passwd : Set for the first time`
    
 
- Go with local installation. So, Please select the `Local` option avilable in the UI.


## Ading the Agent on Docker-Swarm Cluser for monitoring all the containers.

- URL : https://www.portainer.io/installation/


Note: 

    Reference : https://blog.51sec.org/2019/03/install-portainer-in-centos-ubuntu-and.html
