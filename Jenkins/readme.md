
## Jenkins Issue after ( yum update )

- Once I updated the packages then Jenkins stopped working and showing below error.	

Solution : 

 - yum history  --> check when update got happened recentley and note that number

![image](https://user-images.githubusercontent.com/51190838/118772924-e966b580-b8a1-11eb-981e-3480cbf1a806.png)

- Filter the history with number and grep only jenkins and downgarde with old version.

![image](https://user-images.githubusercontent.com/51190838/118773161-2a5eca00-b8a2-11eb-8f7c-917c3925e1b4.png)


## Questions: 

	- Jenkins Workflow Library

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
                    Plugin Info URL : http://afonsof.com/jenkins-material-theme/

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
[!Master_Slave_Configuration_Setup](https://github.com/learn-with-devops/devops/tree/master/Jenkins/Master-Slave-configuration) 
    
## Jenkins Pipeline Types

    - Declarative Pipeline (Jenkins Pipeline)
    
                #!groovy
                branch = env.BRANCH_NAME
		def configmap_env() {
		    if (params.PUSH_DATA_TO == 'KAAS_TO_INT'){
			return [config_env:'se-second-mongo-kaas-to-int-config']
		    }else if (params.PUSH_DATA_TO == 'INT_TO_PREPROD'){
			return [config_env:'se-second-mongo-int-to-preprod-config']
		    }else if (params.PUSH_DATA_TO == 'STAGE_TO_PROD'){
			return [config_env:'se-second-mongo-stage-to-prod-config']
		    }
		}

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
                
                ----------------------------------------------------------------------------------------------------------------
                
                        #!/groovy

                        def branch

                        pipeline{
                            agent any
                            stages{
                                stage('Clean'){
                                    steps{
                                        echo "Deleting workspace"
                                        deleteDir()
                                    }

                                }

                                stage('Checkout'){
                                    steps{
                                        checkout scm
                                        script{
                                            branch = env.BRANCH_NAME
                                            echo "The current branch is ${branch}"
                                        }

                                    }

                                }

                                stage('Compile'){
                                    steps{
                                        script{
                                        sh 'mvn clean compile'

                                        }
                                    }


                                }

                                stage('Testing'){
                                    steps{
                                        script{
                                        sh 'mvn test'
                                        }
                                    }
                                }

                                stage('Build'){
                                    steps{
                                        script{
                                            sh 'mvn package'
                                        }
                                    }
                                }

                                stage('Dev Code Deployment'){
                                    when {
                                        expression { branch == 'dev'}
                                    }
                                    steps{
                                        script{
                                            echo "Development code is deploying"
                                        }
                                    }
                                }

                                stage('Master Code Deployment'){
                                    when {
                                        expression { branch == 'master'}
                                    }
                                    steps{
                                        script{
                                            echo "Production code is deploying"
                                        }
                                    }
                                }
                            }
                        }
    -------------------------------------------------------------------------------------------------------------
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
              
### Variables to shell script

        https://ci.eclipse.org/webtools/env-vars.html/
        Ref : https://stackoverflow.com/questions/41229418/how-to-check-if-a-pipeline-is-triggered-from-a-pull-request
## Jenkins lock

    If you want to lock the jenkins to prevent further executions then you can achive it in two levels
    - Lock Entire Jenkins
    - Lock a Specific Project
    

## Jenkinsfile Syntax Check Reference URL's

    - https://www.eficode.com/blog/jenkins-groovy-tutorial


## Add another pipeline and call from another Job

    stage('call the another pipeline')
		{
			steps {
				build job: 'test-pipeline-child', quietPeriod: 0
				
				or
				
				build job: 'Push-data-from-thread', parameters: [string(name: 'IMAGE_ID', value: "${IMAGE_ID}"), string(name: 'PARENT_BUILD_NUMBER', value: "${BUILD_NUMBER}")]
			}
		}
		
## Change the default Port number, WorkSpace and default user of jenkins

	Go to /etc/sysconfig/jenkins file and change as you want.

## Forgot the password of jenkins
	
	then go to " vi /var/lib/jenkins/users/anand_573465765/config.xml" and find "Passwordhash" section. 
	Replace that hash code with another password known hash code and restart the jenkins. 


## Shared Library

![image](https://user-images.githubusercontent.com/51190838/118755196-1311e380-b886-11eb-87cb-b2c24250b38c.png)

## Ansible playbook Invoking in JenkinsFile

	withCredentials([file(credentialsId: 'ansible_vault_keyfile', variable: 'ansibleVaultKeyFile')]) {
		ansiblePlaybook playbook: 'running-colour.yml', inventory: 'ec2.py', extras: "-e env_name=$environment --vault-password-file ${ansibleVaultKeyFile}"
		}

## Invoke Docker with Jenkins file

	stage('Publish Docker Images to DockerHub')
			{
				steps
				{
					echo "Pushing Docker image to Registory"
					script
					{
						dockerImageTag="$dockerImageRepo"+":"+"$BUILD_NUMBER"
						dockerImage = docker.build "${dockerImageTag}"
						sh 'docker login --username="anandgit71" --password="anandgit12" ${dockerRegistry}'
						dockerImage.push()
					}
				}
			}
