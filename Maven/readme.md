
# Maven Life cycle Phases

![image](https://github.com/learn-with-devops/devops/blob/master/Maven/images/maven-life-cycle-splessons.png)

      validate - validate the project is correct and all necessary information is available
      compile - compile the source code of the project
      test - test the compiled source code using a suitable unit testing framework. These tests should not require the code be packaged or deployed
      package - take the compiled code and package it in its distributable format, such as a JAR.
      verify - run any checks on results of integration tests to ensure quality criteria are met
      install - install the package into the local repository, for use as a dependency in other projects locally
      deploy - done in the build environment, copies the final package to the remote repository for sharing with other developers and projects.

# Maven Installation

      ##  Pre requsites Installation

      sudo yum install java-1.8* wget unzip git tree -y

      ## Download the Maven Latest Package 
      cd /opt/
      wget http://apachemirror.wuchna.com/maven/maven-3/3.6.1/binaries/apache-maven-3.6.1-bin.zip

      ## Extract the Package
      unzip apache-maven-3.6.1-bin.zip

      ## Remove the Unwanted Zip file
      rm -rf apache-maven-3.6.1-bin.zip

      ## Export the PATH
            - vi ~/.bash_profile  { Open this file and paste below path }
            - export PATH=/opt/apache-maven-3.6.1/bin:$PATH

      ## Execute below command for better effect of Bash_Profile
      source ~/.bash_profile


## Mavenn Report Generation

      ## Generate a report
      mvn verify
      ## Install APache
      yum install httpd -y
      ## Copy the reports to Apapche
      cp -pr target/site/jacoco-both /var/www/html/
      ## Start the Apache
      service httpd start
      ## View the Result ( Open 80 port)
      <IP ADdress>:80/jococo-both
      

## Execute maven commands with the below format..

      mvn clean
      
      mvn validate compile test package verify install build
      

- Export Maven path 

      export PATH=/opt/apache-maven-3.6.1/bin:$PATH

      or add the path into .bashrc file and do "source .bashrc" file 
  
  
  
  Example : 
  
      1. For Creating the JAR and execute unit test case , Intigration test case and generate a test case report with the following file.

         https://github.com/LableOrg/java-maven-junit-helloworld
         
         java -cp target/java-maven-junit-helloworld-2.0-SNAPSHOT.jar com.example.javamavenjunithelloworld.HelloApp


      2.  Craete WAR file and deploy into the destination server with tomcat


         https://github.com/sebsto/webapp
         
         # Copy the WAR file to tocat WebApps and restart the server
         
         -- Deploy Jenkins with War file Directly
         
         java -jar jenkins.war
         
         
      3.  Execute Jar file with required dependencies.
      
         https://start.spring.io/
         
         https://github.com/khoubyari/spring-boot-rest-example
         
         java -jar jarfilename.jar
         

- Tomcat Softlink Installation

        ln -s /opt/apache-tomcat-7.0.94/bin/shutdown.sh /usr/bin/tomcatdown
        ln -s /opt/apache-tomcat-7.0.94/bin/startup.sh /usr/bin/tomcatup
  
- Tomact Administartion
  
        <role rolename="admin"/>
        <role rolename="admin-gui"/>
        <role rolename="manager"/>
        <role rolename="manger-gui"/>
        <user username="anand" password="anand" roles="admin,admin-gui,manager,manager-gui"/>
