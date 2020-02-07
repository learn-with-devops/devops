## Linux Scripting Scenarios


  - Check If a Process is Running ?? If not Make it Run otherwise "Print Process is Running" ??
  - Delete files older than 10 days using shell script in Unix [duplicate] ??
  - Take a Backup of Old logs more than 60+ days ??
  - Read Input from Bash CLI ??
  - Read the File line by line ??
  
  

----------------------------------

## Others
  - Check if number is odd or even?
  - How to check number is prime or not?
  - Reverse a String ?
  - Check If String is palindrome ?
  - Search a number in array ?
  - Find missing number in array ?
  - ind duplicate characters/words in the String?
  
  
## Linux

  - xargs
  
        Xargs is a great command that reads streams of data from standard input, then generates and executes command lines; meaning it can take output of a command and passes it as argument of another command. If no command is specified, xargs executes echo by default. You many also instruct it to read data from a file instead of stdin.
        
          1] echo "anand" | xargs mkdir
             o/p : anand dir will create

          2] ls -ltr | xargs
            o/p: It will listout all the output into one line

          3] Remove a file name end with .html
            find . -name "*.html" -type f -print | xargs rm -f

          4] find lins/words/charecters in all files
             ls | xargs wc

    - test (test that lets you do most of these comparisons and tests )

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
      
 - lsof - list open files
 
          lsof meaning ‘LiSt Open Files’ is used to find out which files are open by which process. As we all know Linux/Unix considers everything as a files (pipes, sockets, directories, devices etc). One of the reason to use lsof command is when a disk cannot be unmounted as it says the files are being used. With the help of this command we can easily identify the files which are in use.
          
          
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
      
  - 
  
