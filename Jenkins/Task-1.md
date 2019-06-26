#### -  Maven installation , Softlink
#### -  TOmcat Installation and Softlink

#### -  Create a Pipeline Job ---Scripted pipeline
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
                  
#### Create a file link this "/opt/docker_installation.sh"

          - Remove old war file from Tomcat
          - Copy the latest WAR file from Target folder to TomCat apache webapp folder
          - Restart the Tomcat Apache




##### Reference Script

            node {

                stage('Cleaning the WorkSpace')
                {
                    deleteDir()
                }

                stage('Checkout the code from GitHub')
                {
                    git url: 'https://github.com/anand204/Education.git'
                }

                stage('remove the old code from job')
                {
                    sh 'sudo rm -rf /var/www/html/*'
                }

                stage('Deploying the latest code')
                {
                    sh 'sudo cp -pr /var/lib/jenkins/workspace/Scripted_Pipline_job/* /var/www/html/'
                }
                stage('Restart the Apache')
                {
                    sh 'sudo service httpd restart'
                }
            }
