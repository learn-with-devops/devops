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
    
