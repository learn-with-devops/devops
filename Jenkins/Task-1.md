### Maven installation , Softlink
### TOmcat Installation and Softlink

### Create a Pipeline Job ---Scripted pipeline
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
