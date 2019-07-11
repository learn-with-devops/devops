## Configuration Management Tool -- Ansible

![image](https://github.com/learn-with-devops/devops/blob/master/Ansible/images/ansible-main.png)
![image](https://github.com/learn-with-devops/devops/blob/master/Ansible/images/tasks.PNG)



Aansible Roles
--------------------------------------------------------------
In Ansible, the role is the primary mechanism for breaking a playbook into multiple files. This simplifies writing complex playbooks, and it makes them easier to reuse. The breaking of playbook allows you to logically break the playbook into reusable components.

[root@ip-172-31-4-255 ~]# tree test879
test879
+-- defaults                   --- It override all the variables
¦   +-- main.yml
+-- files                      --  Store
+-- handlers
¦   +-- main.yml
+-- meta                       --- For Informational prpuose (like author info ,company , licence and Platform or OS informatin)
¦   +-- main.yml
+-- README.md                  --- Informational prpuose (about the Role, requirements,dependencies)
+-- tasks
¦   +-- main.yml
+-- templates
+-- tests
¦   +-- inventory
¦   +-- test.yml
+-- vars
    +-- main.yml
