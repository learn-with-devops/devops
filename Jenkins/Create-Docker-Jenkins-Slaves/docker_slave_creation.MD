

## Create a Docker Jenkins slave with Docker Installed inside of the Jenkins slave.

Step1  : 

    - Install Docker Plugin on Jenkins.

Step2 : 
  
    - Expose docker API default port 2375 to another port
      docker run -p 3375:2375 -v /var/run/docker.sock:/var/run/docker.sock -d shipyard/docker-proxy ( or) anandgit71/qube-project:docker-proxy
      
    - Then Test the API listning or not from Master Jenkins node.
      
        - Login to the jenkins master node / server
        - curl http://ipaddress_of_server:3375/v1.40/info   --> if it give responce then it will be good

        Note : v1.40 version you can find by running "docker info" option.
        
Step3: 

  - Go to the jenkins and do the follow
[!image](https://github.com/learn-with-devops/devops/blob/master/Jenkins/Create-Docker-Jenkins-Slaves/Screenshot%20(16).png)
