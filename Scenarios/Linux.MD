Linux Interview Scenarios :
---------------------------

1> Check If a Process is Running ?? If not Make it Run otherwise "Print Process is Running" ??

	Solution 1 :
	------------
	
		#!/bin/bash
		service=replace_me_with_a_valid_service

		if (( $(ps -ef | grep -v grep | grep $service | wc -l) > 0 ))
		then
		echo "$service is running!!!"
		else
		/etc/init.d/$service start
		fi
		
	Solution 2:
	-----------
		#!/bin/bash

		ps -ef | grep -v grep | grep nginx

		if [ $? -eq 1 ]
		then
				echo " Httpd is Stopped !! We are starting the service now"
				sudo service httpd restart
		else
				echo "still running"
		fi
		
2> Delete files older than 10 days using shell script in Unix [duplicate]

		find ./my_dir -mtime +10 -type f -delete
		
		EXPLANATIONS

		./my_dir your directory (replace with your own)
		-mtime +10 older than 10 days
		-type f only files
		-delete no surprise. Remove it to test your find filter before executing the whole command
		
		Example:
		 
		 find /var/log/ -mtime +60 -type d
		 
		 
		 
3> Shell Script to get exception from logs for last one hour

		 grep "^$(date -d -1hour +'%Y-%m-%d %H')" test.logs | grep 'exception'
		 
	


Solve the below linux Interview Questions and let me know for any issue.
------------------------------------------------------------------------

- Find a word in a specific file ??

- We have lot of files inside a /root folder. Find a file which is containig a perticular word??
- Replace a word in a pericular file ??
- Replace a word with first occurence in a file ??
- Find a perticular file in folder-inside-folder ??
- Find a file with less a than 2mb size && greter than 5mb size??
- find files that have a modification time of a day ago ??
- Find a Directory with a specific name ??
- How to add a line of code in the exit file (No need to effect the existing code in the same file) ?? 
- List out top 5 CPU consuming proesses ??
- Check a process is running howmuch long ??
- diff b/w $* and $& ??
- Exclude a String in a file and print ??
- zip and tar a file ?? unzip a zip/tar file??
- Find the modified files in specified time ??
- Count number lines a file??
- Find the last 10 recent logs ??
- Print second word of every line ??
- Find number of CPU cores prasent in Servers ??? //nproc or cat /proc/cpuinfo ??
