#  Jenkins

## Jenkins Installation

    - Create a file with .sh extension
    
   - Copy the content from [here](https://github.com/learn-with-devops/devops/blob/master/Jenkins/Jenkins-Installation-with-yum.sh) to that generated file.
    
    - Give Execute permission to that file.
      chmod 755 filename.sh
    
    - Finally Execute the file
      sh filename.sh


## GitHub-WebHook setup 
    http://13.127.145.152:8080/github-webhook/  
    
##  Email Notification Setup 

![image](https://github.com/learn-with-devops/devops/blob/master/Jenkins/images/email-setup.PNG)

## Plugin Installation

   We have different ways to achive that.
   - Install plugins from avilable section 
   - Download the required version of piugin from https://plugins.jenkins.io/ then upload by using advanced option.
   - Download the required version of piugin from https://plugins.jenkins.io/ then Directly copt to the Plugin section with command prompt.

## Sample Theame Plugin Installation

    Install Jenkins Simple Theme Plugin

    Click Manage Jenkins

    Click Configure System and scroll down to Theme

    Specify the URL for 
    
                    http://afonsof.com/jenkins-material-theme/dist/material-teal.css

    Click Save

## Jenkins Deployent Script

    sudo mkdir -p /opt/flipkart
    cd /opt/flipkart
    sudo rm -rf Billing 
    sudo git clone -b $env https://5b181bf145e1893d3a2d00ae225c3c4b10fcfb64@github.com/flipkartnew/Billing.git
    cd /opt/flipkart/Billing
    sudo service httpd stop
    sudo rm -rf /var/www/html/*
    sudo cp -pr * /var/www/html/
    sudo service httpd start
    

## Jenkins Backup

    We can take Jenkins Backup in different way. In that some of the ways are .. 
    
    - By Using Plugings
            . Thin Backup Plugin
            . Backup Plugin
            
    - By Taking entire jenkins folder as zip and storing some where with ShellScript by scheduling with cronjobs( like in AWS S3 , Nexus and In your local AWS )

## Jenkins Master Slave Configuration
![Master_Slave_Configuration_Setup](https://github.com/learn-with-devops/devops/tree/master/Jenkins/Master-Slave-configuration) 
    
## Jenkins Pipeline Types

    - Declarative Pipeline (Jenkins Pipeline)
    
                #!groovy
                branch = env.BRANCH_NAME

                pipeline
                {
                    agent any
                    stages
                    {
                        stage('clean')
                        {
                            steps
                            {
                                deleteDir()
                                echo "Cleaning completed"
                            }

                        }

                        stage('Checkout')
                        {
                            steps
                            {
                                checkout scm
                                echo "Cloning the latest code from GitHub"
                                script{
                                        echo "Script is executing now"
                                        echo "${branch}"
                                }
                            }			
                        }

                    }	

                    post {

                        always {
                            echo "Build Complted"
                        }
                        aborted {
                            echo "BUILD ABORTED"
                        }
                        success {
                            echo "BUILD COMPLETED SUCCESS"
                        }
                        unstable {
                            echo "BUILD IS UNSTABLE"
                        }
                        failure {
                            echo "BUILD GOT FAILED"
                        }
                    }
                }
    - Scripted Pipeline (Through code)
    
            node{

                stage 'clean'

                deleteDir()

                stage 'checkout'

                git url: 'https://github.com/sebsto/webapp.git'

                stage 'compile'

                sh 'mvn compile'

                stage 'build'

                sh 'mvn package'

                stage 'deploy'

                sh 'sh /opt/docker_installation.sh'
              }
    
## Jenkins lock

    If you want to lock the jenkins to prevent further executions then you can achive it in two levels
    - Lock Entire Jenkins
    - Lock a Specific Project
    
    
