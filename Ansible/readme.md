## Configuration Management Tool -- Ansible

![image](https://github.com/learn-with-devops/devops/blob/master/Ansible/images/ansible-main.png)

Ansible Adhoc Mode
--------------------------------------------------------------
Ad hoc commands are commands which can be run individually to perform quick functions. These commands need not be performed later.

Syntax-1:

    Ansible { group name/server name }  - I { inventory/host name } –m { module } 
    Ex:  ansible web -i inventory -m ping

Syntax-2:

    Ansible { group name/server name }  - I { inventory/host name } –m { module } -a {specify what you want}
    Ex:  ansible web -i inventory -m yum -a "name=httpd state=latest" -b
    note :  -b for become root user

   #### Follow the Ansible Adhoc Mode Example [here](https://github.com/learn-with-devops/devops/blob/master/Ansible/modules_execution_with_Adhoc.md)

Ansible PlayBook
--------------------------------------------------------------
An Ansible playbook is an organized unit of scripts that defines work for a server configuration managed by the automation tool Ansible. Ansible is a configuration management tool that automates the configuration of multiple servers by the use of Ansible playbooks. ... Ansible plays are written in YAML.

Syntax:

         -   Ansible-playbook {playbook name}
         -   Ansible-playbook -vvv {playbook name} 
         -   Ansible-playbook {playbook name} --sysntax-check
         -   Ansible-playbook {playbook name} --check
    
   #### Follow the Ansible Playbook Example [here](https://github.com/learn-with-devops/devops/tree/master/Ansible/Playbooks)
    
Aansible Roles
--------------------------------------------------------------
In Ansible, the role is the primary mechanism for breaking a playbook into multiple files. This simplifies writing complex playbooks, and it makes them easier to reuse. The breaking of playbook allows you to logically break the playbook into reusable components.

![image](https://github.com/learn-with-devops/devops/blob/master/Ansible/images/tasks.PNG)

Syntax:

    ansible-galaxy [delete|import|info|init|install|list|login|remove|search|setup] {file name}

   #### Follow the Ansible Role Example [here](https://github.com/learn-with-devops/Ansible-Role-Apache)


Run Multiple Ansible Tasks under Single condition 
----------------------------------------------------------------

Note:  This can Achive be achived by "block" option in Ansible.
- You can do the Exception Handling also wih the "block", "rescue", "always" modules.

  ref : https://docs.ansible.com/ansible/latest/user_guide/playbooks_blocks.html
 

        - name: Check if Java 8 is instaled
          stat: path=~/java/oraclejdk8
          register: oraclejdk8_sym

        - block:   
            - name: Download Java 8
              command: "wget --no-cookies -O {{ jdk_download_path }}/{{ oraclejdk8.jdk_rpm_file }} --no-check-certificate --header 'Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-cookie' {{ oraclejdk8.jdk_rpm_url }}"

            - name: Install Java 8
              yum: name={{ java_archive }} state=present

            - name: Symlink to ~/java/oraclejdk8
              file: path=~/java/ state=directory mode=0755
            - command: "ln -s /usr/java/jdk{{ oraclejdk8.jdk_version  }} ~/java/oraclejdk8"


            - name: Clean up
              file: state=absent path={{ jdk_download_path}}/{{ oraclejdk8.jdk_rpm_file }}

          when: oraclejdk8_sym.stat.islnk is not defined
          
Example 2: 

                - name: Attempt and graceful roll back demo
                  block:
                    - name: Print a message
                      ansible.builtin.debug:
                        msg: 'I execute normally'

                    - name: Force a failure
                      ansible.builtin.command: /bin/false

                    - name: Never print this
                      ansible.builtin.debug:
                        msg: 'I never execute, due to the above task failing, :-('
                  rescue:
                    - name: Print when errors
                      ansible.builtin.debug:
                        msg: 'I caught an error'

                    - name: Force a failure in middle of recovery! >:-)
                      ansible.builtin.command: /bin/false

                    - name: Never print this
                      ansible.builtin.debug:
                        msg: 'I also never execute :-('
                  always:
                    - name: Always do this
                      ansible.builtin.debug:
                        msg: "This always executes"
                        
                        
                        
 If Else condition with Ansible include
 ---------------------------------------
 
                - name: Check certs exist
                  stat: path=/etc/letsencrypt/live/{{ rootDomain }}/fullchain.pem
                  register: st

                - include: "{{ './_common/check-certs-renewable.yaml' if st.stat.exists else './_common/create-certs.yaml' }}"
                
                
                
how-to-run-only-one-task-in-ansible-playbook
--------------------------------------------

        ---
        hosts: localhost
        tasks:
         - name: Creating s3Bucket
           s3_bucket:
                name: ansiblebucket1234567890
           tags: 
               - createbucket

         - name: Simple PUT operation
           aws_s3:
               bucket: ansiblebucket1234567890
               object: /my/desired/key.txt
               src: /etc/ansible/myfile.txt
               mode: put
           tags:
              - putfile

         - name: Create an empty bucket
           aws_s3:
               bucket: ansiblebucket12345678901234
               mode: create
               permission: private
           tags:
               - emptybucket
               
  Note : 
  
        To ececute a specific task at ansible then use tags like below
        
            ansible-playbook creates3bucket.yml --tags "createbucket,putfile"
            
            
![image](https://user-images.githubusercontent.com/51190838/118757547-f0ce9480-b88a-11eb-9db6-9c9cc22094c1.png)

### Limit the Servers or groups

![image](https://user-images.githubusercontent.com/51190838/118757604-0b087280-b88b-11eb-9211-04e3feed42ca.png)

### Default Groups ( all | ungrouped )
There are two default groups: all and ungrouped. The all group contains every host. The ungrouped group contains all hosts that don’t have another group aside from all.

- Inventory Aliases : 

        jumper ansible_port=5555 ansible_host=192.0.2.50

- Assign variables

        [atlanta]
        host1 http_port=80 maxRequestsPerChild=808
        host2 http_port=303 maxRequestsPerChild=909
        
        Another Example 👎
        [ group ]
        some_host         ansible_port=2222     ansible_user=manager
        aws_host          ansible_ssh_private_key_file=/home/example/.ssh/aws.pem
        freebsd_host      ansible_python_interpreter=/usr/local/bin/python
        ruby_module_host  ansible_ruby_interpreter=/usr/bin/ruby.1.9.3

- Assign variables in group level

  If all hosts in a group share a variable value, you can apply that variable to an entire group at once. 

        [atlanta]
        host1
        host2

        [atlanta:vars]
        ntp_server=ntp.atlanta.example.com
        proxy=proxy.atlanta.example.com

- Inherits the groups and values

        [atlanta]
        host1
        host2

        [raleigh]
        host2
        host3

        [southeast:children]
        atlanta
        raleigh

        [southeast:vars]
        some_server=foo.southeast.example.com
        halon_system_timeout=30
        self_destruct_countdown=60
        escape_pods=2

- Uning multiple inventory sources 

        ansible-playbook get_logs.yml -i staging -i production

- Use one playbook output to another variable

    We can achive this by "Registring dummy host ahd hostvars variable". See the below example.

    Playbook 1:-

        ---
        - hosts: localhost
          gather_facts: false

          tasks:
           - name: Register a new value
             shell: echo "/etc/resolv.conf"
             register: PLAY1VAR

           - debug: msg="{{PLAY1VAR.stdout}}"

           - name: Register dummy host with variable
             add_host:
               name: "DUMMY_HOST"
               PLAY1VAR_NEW: " {{ PLAY1VAR.stdout }}"

    Playbook 2: -

        ---
        - hosts: 192.168.3.151
          gather_facts: false

          tasks:
           - name: Echo the output - PLAY1 variable vaule
             shell: cat {{ hostvars['DUMMY_HOST']['PLAY1VAR_NEW'] }} |tail -1
             register: PLAY2_RESULTS

           - debug: msg="{{PLAY2_RESULTS.stdout}}"

    Example 2 :
    
        - hosts: localhost
          tasks:

            - command: /bin/echo "this is a test"
              register: foo


        - hosts: anotherhost
          tasks:
            - debug: var=foo
              when: foo is defined

            - debug: var=hostvars['localhost']['foo']
              when: hostvars['localhost']['foo'] is defined
    
## CMD vs Shell
![image](https://user-images.githubusercontent.com/51190838/120961332-4526af00-c77b-11eb-9fc4-546ba4c9e757.png)

## Encrypt the values with Ansible.

#####  Ansible Valut is useful here

![image](https://user-images.githubusercontent.com/51190838/121057069-81d6c280-c7dc-11eb-996c-bc96c7e5fc80.png)
![image](https://user-images.githubusercontent.com/51190838/121057124-92873880-c7dc-11eb-8567-a5122e30c038.png)
![image](https://user-images.githubusercontent.com/51190838/121057217-ac288000-c7dc-11eb-9dd2-d268ceb30ad4.png)
![image](https://user-images.githubusercontent.com/51190838/121057356-d0845c80-c7dc-11eb-9ee3-2ae5ef7e61ae.png)

Use the password in a file like this : 

    -> ansible --ask-vault-pass
    -> echo 'my_vault_password' > .vault_pass
    -> ansible --vault-password-file=.vault_pass -bK -m copy -a 'src=secret_key dest=/tmp/secret_key mode=0600 owner=root group=root' localhost
    -> ansible.cfg

        [defaults]
        . . .
        vault_password_file = ./.vault_pass


### Ansible variable precedence
<img width="442" alt="Screenshot 2023-04-19 at 5 17 38 PM" src="https://user-images.githubusercontent.com/51190838/233065747-9cd3db76-94c0-44e7-a4a5-965994681170.png">

### what is Ansible Set_Fact ??

Ansible set_fact is a module, which is going to be used like vars, vars_file etc. But, this set_facts has the high precedence than others except extra variables.

Also, this set_fact module will be load once and the same value will be there across for all calls.

