## While Condition with Loop Nesting

            #! /bin/sh

            a=0

            while [ "$a" -lt 10 ]
            do 
               b="$a"
               while [ "$b" -ge 0 ]
               do
                  echo -n "$b "
                  b=`expr $b - 1`
               done
               echo
               a=`expr $a + 1`
            done
            
 Output: 
 
            0 
            1 0 
            2 1 0 
            3 2 1 0 
            4 3 2 1 0 
            5 4 3 2 1 0 
            6 5 4 3 2 1 0 
            7 6 5 4 3 2 1 0 
            8 7 6 5 4 3 2 1 0 
            9 8 7 6 5 4 3 2 1 0



## For loop to print 10 numbers

    Scenario 1:
    
            #!/bin/bash

            for (( i=0; i<10; i++ ))
            do
             echo $i
            done
            
    Scenario 2:
    
            #!/bin/bash
            for i in 1 2 3 4 5
            do
              echo -n "$i "
            done
            
            Note : 
                        -n --> for single line output
            
            
            
         
