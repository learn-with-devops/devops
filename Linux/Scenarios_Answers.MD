## Check If a Process is Running ?? If not Make it Run otherwise "Print Process is Running" ??


        Solution  :
        ------------

                #!/bin/bash
                service=replace_me_with_a_valid_service

                if (( $(ps -ef | grep -v grep | grep $service | wc -l) > 0 ))
                then
                echo "$service is running!!!"
                else
                /etc/init.d/$service start
                fi
