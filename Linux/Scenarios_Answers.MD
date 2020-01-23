## 1. Check If a Process is Running ?? If not Make it Run otherwise "Print Process is Running" ??


        Solution :
        ------------

                #!/bin/bash
                service=replace_me_with_a_valid_service

                if (( $(ps -ef | grep -v grep | grep $service | wc -l) > 0 ))
                then
                echo "$service is running!!!"
                else
                /etc/init.d/$service start
                fi


## 2. Delete files older than 10 days using shell script in Unix [duplicate] ??

       Solution : 
       ------------
       
               find ./my_dir -mtime +10 -type f -delete
                
               '''
                EXPLANATIONS

                ./my_dir your directory (replace with your own)
                -mtime +10 older than 10 days
                -type f only files
                -delete no surprise. Remove it to test your find filter before executing the whole command

                Example:

                 find /var/log/ -mtime +60 -type d
                 
               '''
