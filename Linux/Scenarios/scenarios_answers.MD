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

       Solution 1: 
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
               
        Solution 2:
        ------------
        
                find /root/anand/ -mtime +60 -type f -exec rm -f {} \;
                
                
## 3. Take a Backup of Old logs more than 60+ days ??

                
        Solution 1:
        -----------
        
                #!/bin/bash

                set -x 

                #Script -Purpose:Backup script
                # Exits with zero if no error.


                # Step -1 Function to archieve file using date and time

                date=`/bin/date "+%Y.%m.%d.%H.%M.%S"`

                echo $date

                mkdir -p /root/backup_folder/$date

                find /root/anand/ -type f -iname "*.log" -mtime +60 -print |xargs -I {} mv {} /root/backup_folder/$date

                tar -cvzf /root/$date.tar.gz /root/backup_folder/$date
                
                
 ## 4. Read the Input from CLI ??
 
                #!/bin/sh
                echo "what is your name?"
                read name
                echo "How do you do, $name?"
                read remark
                echo "I am $remark too!"
