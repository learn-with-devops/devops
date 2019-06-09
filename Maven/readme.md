

- Export Maven path 

      export PATH=/opt/apache-maven-3.6.1/bin:$PATH

      or add the path into .bashrc file and do "source .bashrc" file 
  
  
  
  Example : 
  
      1. For Creating the JAR and execute unit test case , Intigration test case and generate a test case report with the following file.

         https://github.com/LableOrg/java-maven-junit-helloworld
         
         java -cp target/java-maven-junit-helloworld-2.0-SNAPSHOT.jar com.example.javamavenjunithelloworld.HelloApp


      2.  Craete WAR file and deploy into the destination server with tomcat


         https://github.com/sebsto/webapp
         
         
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
