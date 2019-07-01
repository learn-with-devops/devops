Adhoc Mode 
==========

- Ping (For checking the remote server health)

  ansible appgroup -m ping

- File (For Creating the File/Folder)

  ansible appgroup -m file -a "path=/root/anand state=directory owner=root group=centos " -b

- Yum (For Software Installation)

  ansible appgroup -m yum -a "name=httpd state=latest"

- Service

  ansible appgroup -m service -a "name=httpd state=started"

- Shell 

  ansible appgroup -m service -a "name=httpd state=started"

- Copy

  ansible appgroup -m copy -a " src=/etc/passwd dest=/root"

- User

  ansible appgroup -m copy -a " src=/etc/passwd dest=/root"

- Group

  ansible appgroup -m copy -a " src=/etc/passwd dest=/root"

- Git

  ansible appgroup -m git -a "repo=https://github.com/sebsto/webapp.git dest=/root/github"

- Setup

  ansible appgroup -m setup

  ansible appgroup -m setup -a "filter=ansible_distribution"
