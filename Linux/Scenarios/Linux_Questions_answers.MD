## Linux_Insterview Questions Answers

## How to exclude the package from yum update

   - You can perform "yum update --exclude=kernel* --exclude=php*"

   -  Also, you can specify the same on "/etc/yum.conf" 
   
	[main]
	cachedir=/var/cache/yum/$basearch/$releasever
	keepcache=0
	debuglevel=2
	logfile=/var/log/yum.log
	exactarch=1
	obsoletes=1
	gpgcheck=1
	plugins=1
	installonly_limit=5
	exclude=kernel* redhat-release* php* mysql* httpd* 

## Upgrading the Package 
  
   Link : https://www.prado.lt/5-minute-upgrade-nginx-1-12-to-1-17-on-centos-7-rhel-7

## How to close vi file which alredy opened and forgot to close.

   option 1 : Kill the vi process
   Option 2:  remove the .swp file 

## How to increse the number of files to open in linux:
---------------------------------------------------

to increase open file limit to 500000, you can use the following command as root:

	sysctl -w fs.file-max=500000
	
	# cat /proc/sys/fs/file-max
	
		Note: With the above command the changes you have made will only remain active until the next reboot. If you wish to apply them permanently, you will have to edit the following file:
		
		# vi /etc/sysctl.conf
		
		Add this line in file : 
			fs.file-max=500000

ulimit :
--------------------------

ulimit is admin access required Linux shell command which is used to see, set, or limit the resource usage of the current user. It is used to return the number of open file descriptors for each process. It is also used to set restrictions on the resources used by a process.

ulimt -u
ulimit -a   -> for all

- showing the maximum file size a user can have.
	ulimt -f
	
- To display maximum users process or for showing maximum user process limit for the logged-in user.
	ulimit -u
	
- Set Ulimit temporarley
	ulimit -u 12345

- Set Ulimit permanentley 
	vim /etc/security/limits.conf


/var/log/messages
-------------------------

The most important log file in Linux is the /var/log/messages file, which records a variety of events, such as the system error messages, system startups and shutdowns, change in the network configuration, etc.
	

- Service account in k8s.
- how to upgrade k8s


How to check the remote server port open or not
-----------------------------------------------

-> netcat

	nc -zvw3 192.168.1.8 22
		nc: It’s a command.
		z: zero-I/O mode (used for scanning).
		v: For verbose.
		w3: timeout wait seconds
		192.168.1.8: Destination system IP.
		22: Port number needs to be verified.
		
-> nmap
	
	nmap 192.168.1.8 -p 22
	
-> telnet

	telnet 192.168.1.9 22


How to Identify the Ip addr is a Private or Public
---------------------------------------------------

Below lenth got reserved for Private Network

		192.168.0.0 - 192.168.255.255 (65,536 IP addresses)
		172.16.0.0 - 172.31.255.255 (1,048,576 IP addresses)
		10.0.0.0 - 10.255.255.255 (16,777,216 IP addresses)

Check CPU utilization
--------------------------

   mpstat
   
Check Subnet Mask address
-----------------------------

	netstat -r

Modify a file located in Remote server:
-----------------------------------

	ssh -t user1@computer1 'vim /path/laboratory_notebook_1.md'

		-t = force sudo
		
Copy files to remote server:
-----------------------------

	we have lot of ways like scp , sftp , rsync etc
	
	scp : 
	
		scp -r file/folder user1@computer1:/path/
		
Find a Word
------------
- Find a word in a file

	  grep "word" filename

- Find a Word in a folder-inside-folder and file
  	
	  grep -Rw /home/reddredd/ -e "apk update"

  -R == read all files under each directory, recursively
  -w == Select only those lines containing matches that form whole words
  -e == specify the string (pattern) to be searched
  
- Print the output execpt a word containig words 
  
 	 grep -v "anand" filename.txt

Repalce a Word
------------

- sed -i 's/original/new/g' file.txt

	Explanation:

		sed = Stream EDitor
		-i = in-place (i.e. save back to the original file)
		The command string:

		s = the substitute command
		original = a regular expression describing the word to replace (or just the word itself)
		new = the text to replace it with
		g = global (i.e. replace all and not just the first occurrence)
		file.txt = the file name

- Replace a word in first accurence
	
  	sed -i 's/original/new/1' file.txt
  
- Replace a word in Second accurence
  
  	sed -i 's/original/new/2' file.txt

Find a File
------------

- Find an Empty file

  	find . -type f -empty

- Find a file
  
  	find / -type f -name *.cer

- find -name "test*"

- find -iname "query"  // -iname is for ignoring the case sensitive

- Find a file with less than a specified size
  	
	  find / -size -50c

		c: bytes
		k: Kilobytes
		M: Megabytes
		G: Gigabytes
		b: 512-byte blocks

- Find a file with Greater than a specified size
  
  	find / -size +700M
  
- Find a file less than perticula size
  
  	find . -type f -size -1M

- Finding by Owner and Permissions
  
  	find / -perm -644

- Time
	Linux stores time data about access times, modification times, and change times.

	Access Time: Last time a file was read or written to.
	Modification Time: Last time the contents of the file were modified.
	Change Time: Last time the file's inode meta-data was changed.

   - To find files that have a modification time of a day ago, type:
   
   	  find / -mtime -1
     

   - If we want files that were accessed in less than a day ago, we can type:
     
     	find / -atime -1
     
   - Find the files created by a perticular interval
     
     	find /root -newermt "2018-01-01" ! -newermt "2019-11-23"

Find a Directory
----------------

- find . -type d -name "node_mo*"

Find a Logs 
-----------

- tail -fn 100 filename

- head -n 10 filename  or pr -10 filename



Print perticular position of the Word:
--------------------------------------

- Print second word of every line

	  awk {'print $2'}

- Print the match word

  	awk '/manager/ {print}' employee.txt
  	awk '/RUN/ {print $1,$2}' Dockerfile

- awk '{print $1,$2}' Dockerfile

count the lines in a file
-------------------------

- awk 'END {print NR}' Dockerfile

- wc -l Dockerfile

Find the modified files in specified time
-----------------------------------------
- find . -type f -newermt "2019-01-22 00:00:00" \! -newermt "2019-02-22 13:23:00"
- find /root -newermt "2018-01-01" ! -newermt "2019-11-23"



Zip a file 
-----------
- tar -czvf archive.tar.gz  FolderName
  tar -cvzf ssl.tar.gz ssl

Unzip a file
--------------
- tar -xzvf archive.tar.gz
- tar -xvzf ssl.tar.gz -C /home/ananddxr
or
- tar -xvf articles.tar --directory /tmp/my_articles/

Adding a single line by end of the file
---------------------------------------
- sed -e "\$a/dev/xvdb /mount1 ext4 defaults,nofail 0" /etc/fstab
- echo "/dev/xvdb /mount1 ext4 defaults,nofail 0" >> /etc/fstab

Top 5 CPU consuming processes:
--------------------------------------

	ps -Ao user,pcpu,pid,uid,%mem --sort=-%mem |head -n 5
	
	-e     Select all processes.  Identical to -A.
	-o format
              User-defined format.  format is a single argument in the form of a blank-separated or comma-separated list, which offers a way to specify individual output columns.

Print a Proccess tree:
----------------------

	ps -e --forest  


Check a process is running howmuch long
-------------------------------------
ps -p 129955 -o etime  ---{DD-]hh:]mm:ss.}  --etime[elapsed time since the process was started]

EX:  ELAPSED
8-10:36:54

Exclude a String in a file and print
------------------------------------

grep -v "strin" filename

-v, --invert-match        select non-matching lines

Note: Ignore Multiple Strings

cat test.txt |grep -v -e "anand" -e "shashi" -e "jkhl"

User and Group 
------------------------------------

- find the users list 
  cat /etc/passwd
  
- find the password stored place
  cat /etc/shadow
  
- List of groups
  cat /etc/group
  
Umask
------------------------------------

- Default Umask value 
  0022
  
- Default Umask value for file
  666-022 = 644
  
- Default Umask value for Folder
  777-022 = 755

- Change the Umask value permanently
  vi /etc/bashrc --> chnage in that file
  
ls -ltr && ls -la && ll 
-------
	ls = list directory contents
	
	-l = long listing: lists the mode, link information, owner, size, last modification (time). If the file is a symbolic link, an arrow (-->) precedes the pathname of the linked-to file.
	-t = Sort with the primary key being time modified (most recently modified first) and the secondary key being filename in the collating sequence.
	-r = Reverse the order of the sort to get reverse collating sequence or oldest first
	-a = Write out all directory entries, including those whose names begin with a period ( '.' ). Entries beginning with a period shall not be written out unless explicitly referenced, the -a option is supplied, or an implementation-defined condition shall cause them to be written.


Commands:
-------------------
	$? = The Exist status of last command
	$1,$2..$10 = Parameters
	$0 = File name of the current script
	$# = No.of Arguments supplied to a script
	$$ = Process ID of current shell
	$! = Process number of last executed script
	$* = Gives all the passed arguments as single argument
            
            $ cat 1.sh
            mkdir "$*"

            $ sh 1.sh a "b c" d

            $ ls -l
            total 12
            -rw-r--r-- 1 igor igor   11 mar 24 10:20 1.sh
            -rw-r--r-- 1 igor igor   11 mar 24 10:20 2.sh
            drwxr-xr-x 2 igor igor 4096 mar 24 10:21 a b c d  

$@ = Gives all the passed arguments into separe arguments like below

            cat 2.sh
            mkdir "$@"

            $ sh 2.sh a "b c" d

            $ ls -l
            total 24
            -rw-r--r-- 1 igor igor   11 mar 24 10:20 1.sh
            -rw-r--r-- 1 igor igor   11 mar 24 10:20 2.sh
            drwxr-xr-x 2 igor igor 4096 mar 24 10:21 a
            drwxr-xr-x 2 igor igor 4096 mar 24 10:21 a b c d
            drwxr-xr-x 2 igor igor 4096 mar 24 10:21 b c
            drwxr-xr-x 2 igor igor 4096 mar 24 10:21 d



Port Numbers:
-----------------
	- ssh  22
	- smtp 25
	- SQL server 1433
	- http 80
	- https 443
	- jenkins/Apache TomCat 8080
	- MySQL 3306
	- Oracle 1521
	- FTP 20/21
	- Telnet 23
	- DNS 53
	- DHCP 68
	- Monit 2812
	- Nexus 8081

How to start the service automatically when the server got reboot ??
----------------------------------

	/etc/init.d  == > place original file here
	/etc/rc3.d   == > Create a shart cut here
	
What are the most common Shell types?
----------------------------------

	There are 4 major Shell types: Bourne Shell (sh), C Shell (csh), Korn Shell (ksh) and Bourne Again Shell (bash).
	Of this, the (bash) type is the most frequently used.
	
Cron scheduler command helps you to execute the task on every Monday at 5 AM. This command is helpful for doing weekly tasks like system clean-up.
----------------------------------
 
   	0 5 * * mon  /scripts/script.sh
	
	
Run a Process in BackGround Mode 
--------------------------------

	nohup python gateway_metrics.py
	
	
Write a script to filter the log files and find the maximum number of hits from a specific IP ??
--------------------------------

	cat logfile.log | awk '{print $1}'|sort|uniq -c | tail
	
	cat error_log | awk -F ' ' '{print $10}' | awk -F ':' '{print $1}' | sort | uniq -c
	
	--> F - for field separater 
	

xargs
-----------------------
  
        Xargs is a great command that reads streams of data from standard input, then generates and executes command lines; 
	meaning it can take output of a command and passes it as argument of another command. If no command is specified, 
	xargs executes echo by default. You many also instruct it to read data from a file instead of stdin.
        
		  1] echo "anand" | xargs mkdir
		     o/p : anand dir will create

		  2] ls -ltr | xargs
		    o/p: It will listout all the output into one line

		  3] Remove a file name end with .html
		    find . -name "*.html" -type f -print | xargs rm -f

		  4] find lins/words/charecters in all files
		     ls | xargs wc

test (test that lets you do most of these comparisons and tests )
----------------------------

		  1] check the strings are equal
		      test howto = forge && echo "same" || echo "not"
		      o/p: not

		  2] test 5 -eq 7 && echo "same" || echo "not"
		      o/p : not

		  3] test two files which one created first ??
		    test file1 -nt file2 && echo "newer" || echo "nor"  // -nt --> newer than. 
		    -ot --> older than

		  4] check it is a directory
		    test -d new_dir && echo "yes". // -f --> for file
      
lsof - list open files
----------------------------
 
          lsof meaning ‘LiSt Open Files’ is used to find out which files are open by which process. As we all know Linux/Unix 
	  considers everything as a files (pipes, sockets, directories, devices etc). One of the reason to use lsof command is 
	  when a disk cannot be unmounted as it says the files are being used. With the help of this command we can easily 
	  identify the files which are in use.
          
          
		  1] List User Specific Opened Files
		    lsof -u anand

		  2] Find Processes running on Specific Port
		    lsof -i TCP:8080

		  3] List Open Files of TCP Port ranges 1-1024
		    lsof -i TCP:80-8080

		  4] List all Network Connections
		     lsof -i

		  5] Find Out who’s Looking What Files and Commands?
		    lsof -i -u tecmint

		  6] search by PID
		    lsof -p 1

		  7] Kill all Activity of Particular User
		    kill -9 `lsof -t -u anand`
disk
---------

	  - lsblk ( list of avilable block devices)
	  - blkid ( list out th UUID of block device )

		blkid /dev/xvda1
		o/p: /dev/xvda1: UUID="f41e390f-835b-4223-a9bb-9b45984ddf8d" TYPE="xfs" 
        
pass 10 , 11...argument in a script 
-------------------------------------


		script.sh 1 2 3 4 5 6 7 8 9 anand reddy

		script: 
		  echo $9
		  echo ${10}
		  echo ${11}

		ex: 

		#!/bin/ksh   
		echo There is $# parameters
		while [ $# -ne 0 ]; do
			 echo $1
			 shift
		    done

		o/p: Will:/home> ./script a b c d e f g h i j k l m n o p q r s t u v w x y z
		There is 26 parameters

