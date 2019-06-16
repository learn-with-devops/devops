#  Jenkins 

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

##  Email Notification Setup 

![image](https://github.com/learn-with-devops/devops/blob/master/Jenkins/images/email-setup.PNG)
