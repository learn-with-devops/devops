## Linux_Insterview Questions Answers


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

- head -n 10 filename 



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

