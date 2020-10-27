Ref : https://www.softwaretestinghelp.com/ansible-playbooks-ansible-vaults/

-----
      - name: Create User
         user: name=niranjan password=niranjan groups=ansible shell=/bin/bash
    
##
      - name: Remove User
        user:
        name=niranjan state=absent remove=yes force=yes
    
## 
      - name: Copy content to file
        copy: content="Hello World Niranjan \n" dest=/home/ansible/niranjan.txt
    
## 
      - name: Replace word example
        replace:
         path: /home/ansible/niranjan.txt
         regexp: 'hello'
         replace: "world"
     
##   
      - name: Ansible zip file example
       archive:
        path: /home/ansible/niranjan.txt
        dest: /home/ansible/niranjan.zip
        format: zip
     
## 
      - name: Ansible zip multiple files example
       archive:
        path:
         - /home/ansible/niranjan1.txt
         - /home/ansible/niranjan2.txt
        dest: /home/ansible/niranjan.zip
        format: zip

## 
      - name: Ansible zip directory example
      archive:
       path:
        - /home/ansible
       dest: /home/ansible/niranjan.zip
       format: zip
     
## 
      - name: Date and Time Example in Ansible
        debug:
         var=ansible_date_time.date
     
## 
      - name: Ansible timestamp filename example
        command: touch niranjan{{ansible_date_time.date}}.log
    
## 
