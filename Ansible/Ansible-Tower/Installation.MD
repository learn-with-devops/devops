## Ansible Tower Installation 

### Pre Requisites

        -   Python , wget , epel-release and Ansible
        
              Yum install epel-release wget python ansible -y
            
            
### Minimal Changes

        -   Change the Umask address from 077 to 0022 in the ~/.bashrc file
        
### Download the ansible tower and Install like below.


        - Download the Tower packages
          
            wget http://releases.ansible.com/ansible-tower/setup/ansible-tower-setup-3.1.5.tar.gz
          
        - Extarct that 
        
            tar -xzvf ansible-tower-setup-3.1.5.tar.gz
           
        - Create a Username/Password for UI login like below
        
            cd ansible-tower-setup-3.1.5

            vi inventory   # plase all below code/ change as you required
        
                      [tower]
                       localhost ansible_connection=local

                      [database]

                      [all:vars]
                       admin_password='password'

                       pg_host=''
                       pg_port=''

                       pg_database='awx'
                       pg_username='awx'
                       pg_password='password'

                       rabbitmq_port=5672
                       rabbitmq_vhost=tower
                       rabbitmq_username=tower
                       rabbitmq_password='password'
                       rabbitmq_cookie=cookiemonster

                       # Needs to be true for fqdns and ip addresses
                       rabbitmq_use_long_name=false
                       
                       
### Change the file name

             Chnage the name from 'starting' to 'started' in the ansible-tower-setup-3.1.5/roles/rabbitmq/tasks/main.yml file

### Run the script

             Finally run the ./setup.sh   // Make sure need to allow 443 port for listuning


### Reference Link 
               http://devopstechie.com/install-and-configure-ansible-tower-centos7/
