
Ref : https://www.youtube.com/watch?v=jaaMNK0Df8U

## Create a Docker Jenkins slave with Docker Installed inside of the Jenkins slave.

Initial things : 

    - Install Master jenkins via normal way or as Docker container.
            docker run -td -p 8081:8080 --name Jenkins-Master jenkins/jenkins


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

  - Go to the jenkins and do the follow image steps : 
[!image](https://github.com/learn-with-devops/devops/blob/master/Jenkins/Create-Docker-Jenkins-Slaves/Screenshot%20(16).png)
[!image](https://github.com/learn-with-devops/devops/blob/master/Jenkins/Create-Docker-Jenkins-Slaves/Screenshot%20(17).png)

Step4: 

    - Go to master node and desable number of executers to 0 from 2.\

step5:
    
    - Create a dummy job and execute it to see the dynamic docker slave.
            pipeline {
            agent any

            stages {
                stage('Hello') {
                    steps {
                        echo 'Hello World'
                        sh 'docker --version'
                        sh 'docker info'
                        sh 'docker pull httpd'
                        sh 'docker login --username="anandgit71" --password="anandgit12"'
                    }
                }
            }
        }


Thats it !!
