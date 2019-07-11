## Configuration Management Tool -- Ansible

![image](https://github.com/learn-with-devops/devops/blob/master/Ansible/images/ansible-main.png)

Ansible PlayBook
--------------------------------------------------------------
An Ansible playbook is an organized unit of scripts that defines work for a server configuration managed by the automation tool Ansible. Ansible is a configuration management tool that automates the configuration of multiple servers by the use of Ansible playbooks. ... Ansible plays are written in YAML.

  -   Ansible-playbook {playbook name}
  -   Ansible-playbook -vvv {playbook name} 
  -   Ansible-playbook {playbook name} --sysntax-check
  -   Ansible-playbook {playbook name} --check
    
    #### Follow the Ansible Playbook Example [here](https://github.com/learn-with-devops/devops/tree/master/Ansible/Playbooks)
    
Aansible Roles
--------------------------------------------------------------
In Ansible, the role is the primary mechanism for breaking a playbook into multiple files. This simplifies writing complex playbooks, and it makes them easier to reuse. The breaking of playbook allows you to logically break the playbook into reusable components.

![image](https://github.com/learn-with-devops/devops/blob/master/Ansible/images/tasks.PNG)

   #### Follow the Ansible Role Example [here](https://github.com/learn-with-devops/Ansible-Role-Apache)
