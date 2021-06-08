## All in One page

    ---
     - name: Apache Installation'
       group: web
       vars:
        - devops_users: devops,anand
        - apache_root: opt
       gather_facts: True
       become: True

       tasks:
       - name: create a devops user
         user: 
           name: {{devops_users}}
           group: {{devops_users}}
           home: "/home/{{devops_users}}"
           state: prasent
           createhome: yes

       - name: create a folder for logs storage
         file:
           path: "/{{apache_root}}/httpd"
           owner: {{devops_users}}
           group: {{devops_users}}
           mode: 0755
           state: directory
           recursive: True

       - name: Install rsync
         package: name=rsync state=prasent

       - name: Replace the lins
         replace:
           path: "/etc/ssd/sshd_config"
           regexp: "^PasswordAuthentication no"
           replace: "PasswordAuthentication yes"
         tags:
           - passwdfilechnage

       - name: Add the keys
         authorized_keys:
           user: {{devops_users}}
           state: prasent
           key: {{item}}
         with_items: 
           - "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCYjK5i9qctTayLgwjt6iiPo22kP1tbx4tK1sIJpDcqTiK3352wF0CnpHctCcq6op9ZOxPF8XyEFx5WQlKzez/umFT1bcSct5XjSTEk7iWEp3aKowuRawdF4jhIcqqA2fmqt6JzTPpzUyKuNlWl5YyWNANTSOG6WJ0Eb+Rg0nsjyspFVRU3OKquA5okGrC1Xex4Iv+/qC+2LyIyWxrx6tm8qCo/uTNX6gJyQN0/QE/cUawHmua+j9TsmgxT4gMrR/023srxL4oMbnUxDTu3mplH8k3TLNLEDS2ZizdhOchRj2eHhR/GgDreWPgxcHe+rH7kt30l/0KgIPUV2Yr4MY8CtN0DZuObjLWTgJhjcdp1Ks3wLD9QxVAVAddSd+2cvzc7DRteZOTXv7+opwTepcMZGTFRrbsjgkaUzmcLG46BUZQ7+IrfIEu4NN0nEAwZYrghPludVbBXAz7VUAaTfdtDTOxB6hQEBd42RZsBfka9Mcb5rSS9VuKAn4h9yYUd6pE= Anand_Reddy@epam.com"
           - "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCYjK5i9qctTayLgwjt6iiPo22kP1tbx4tK1sIJpDcqTiK3352wF0CnpHctCcq6op9ZOxPF8XyEFx5WQlKzez/umFT1bcSct5XjSTEk7iWEp3aKowuRawdF4jhIcqqA2fmqt6JzTPpzUyKuNlWl5YyWNANTSOG6WJ0Eb+Rg0nsjyspFVRU3OKquA5okGrC1Xex4Iv+/qC+2LyIyWxrx6tm8qCo/uTNX6gJyQN0/QE/cUawHmua+j9TsmgxT4gMrR/023srxL4oMbnUxDTu3mplH8k3TLNLEDS2ZizdhOchRj2eHhR/GgDreWPgxcHe+rH7kt30l/0KgIPUV2Yr4MY8CtN0DZuObjLWTgJhjcdp1Ks3wLD9QxVAVAddSd+2cvzc7DRteZOTXv7+opwTepcMZGTFRrbsjgkaUzmcLG46BUZQ7+IrfIEu4NN0nEAwZYrghPludVbBXAz7VUAaTfdtDTOxB6hQEBd42RZsBfka9Mcb5rSS9VuKAn4h9yYUd6pE= Anand_Reddy@epam.com"

       - name: Listout the users
         command: cat /etc/passwd

       - block:
            - name: Install Pre-required softwares
              yum: name={{ item }} state=latest
              register: installed_data
              with_items:
                - wget
                - zip
                - tree
                - epel-release
                - httpd

            - name: Clone the repo from git
              git: repo=https://github.com/learn-with-devops/static-website-example.git dest=/var/www/html force=yes
              notify:
              - Restart Apache

            - name: copy config files
              copy: src=/tmp/httpd.conf dest=/etc/httpd/httpd.conf
              notify:
              - Restart Apache

            - name: Get the Apache Installed Version
              debug: msg="{{ installed_data.stdout}}"

            - name: Register with dummy host
              add_host:
                name: "dummy_host"
                installed_data_new: "{{ installed_data.stdout }}"

         when: ansible_distribution == "CentOs"

       handlers:
       - name: Restart Apache
         service: name=httpd state=restarted

-----------------------------------------

tasks:
     - name: Echo the output - PLAY1 variable vaule
       shell: cat {{ hostvars['dummy_host']['installed_data_new'] }} |tail -1
       register: PLAY2_RESULTS


Roles skeleton structure: 

        # Readme.MD
        # Meta
        # files
        # templates
        # vars
        # tests
        # handlers
        # tasks

        # ---
        #  - include: hello.yml
        #    when: ansible_distribution == "Ubuntu"
