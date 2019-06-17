#  Jenkins Index

    - Jenkins user administratation
    - Jenkins Remote Execution
    - Jenkins BackUp

## Jenkins Installation

    - Create a file with .sh extension
    
   - Copy the content from [here](https://github.com/learn-with-devops/devops/blob/master/Jenkins/Jenkins-Installation-with-yum.sh) to that generated file.
    
    - Give Execute permission to that file.
      chmod 755 filename.sh


## GitHub-WebHook setup 
    http://13.127.145.152:8080/github-webhook/  
    
##  Email Notification Setup 

![image](https://github.com/learn-with-devops/devops/blob/master/Jenkins/images/email-setup.PNG)


## Plugin Installation with Sample Theame

    Install Jenkins Simple Theme Plugin

    Click Manage Jenkins

    Click Configure System and scroll down to Theme

    Specify the URL for 
                    http://jenkins-contrib-themes.github.io/jenkins-neo-theme/dist/neo-light.css.

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
    
