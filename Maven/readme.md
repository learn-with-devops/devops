
# Maven Life cycle Phases

![image](https://github.com/learn-with-devops/devops/blob/master/Maven/images/maven-life-cycle-splessons.png)



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
         
         java -jar warfilename.war
         
         
      3.  Execute Jar file with required dependencies.
      
         https://start.spring.io/
         
         https://github.com/khoubyari/spring-boot-rest-example
         
         java -jar jarfilename.jar
         

- Tomcat Softlink Installation

        ln -s /opt/apache-tomcat-7.0.94/bin/shutdown.sh /usr/bin/tomcatdown
  
- Tomact Administartion
  
        <role rolename="admin"/>
        <role rolename="admin-gui"/>
        <role rolename="manager"/>
        <role rolename="manger-gui"/>
        <user username="anand" password="anand" roles="admin,admin-gui,manager,manager-gui"/>
