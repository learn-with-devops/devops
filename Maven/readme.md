

- Export Java path 

      export PATH=/opt/apache-maven-3.6.1/bin:$PATH

      or add the path into .bashrc file and do "source .bashrc" file 
  
  
  
  Example : 
  
      1. For Creating the JAR and execute unit test case , Intigration test case and generate a test case report with the following file.

         https://github.com/LableOrg/java-maven-junit-helloworld


      2.  Craete WAR file and deploy into the destination server with tomcat


         https://github.com/sebsto/webapp

  
  
- Tomact Administartion
  
        <role rolename="admin"/>
        <role rolename="admin-gui"/>
        <role rolename="manager"/>
        <role rolename="manger-gui"/>
        <user username="anand" password="anand" roles="admin,admin-gui,manager,manager-gui"/>
