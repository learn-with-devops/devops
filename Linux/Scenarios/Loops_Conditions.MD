![image](https://github.com/learn-with-devops/devops/blob/master/Linux/images/conditions.jpg)
 
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



## For/While loop to print 10 numbers

    Scenario 1 with For:
    
            #!/bin/bash

            for (( i=0; i<10; i++ ))
            do
             echo $i
            done
            
    Scenario 2 with For:
    
            #!/bin/bash
            for i in 1 2 3 4 5
            do
              echo -n "$i "
            done
            
            Note : 
                        -n --> for single line output
                        
    Scenario 3 with For :
    
            #! /bin/bash

            for i in {1..100}
            do
              echo $i
            done
                        
    Scenario 4 with While : 
    
            #!/bin/bash

            j=1

            while [ $j -le 10 ]
            do
               echo -n  $j
               j=$(( $j + 1 )) # increse the count in another way like == > a= ` expr a + 1 ` or let a=a+1"
            done
            
            
 ## If Condition
 
    Scenario 1 :
    
            #!/bin/bash
            a=10
            b=100
            if (( $a == $b ))
            then
               echo " $a and $b are equal"
            else
               echo " $a and $b are not equal"
            fi
            
 
 ## IF-else-If condition
 
      Scenarion 1 : 
      
            #! /bin/bash

            if [ $1 -gt 18 ]
            then
               echo "You may go to the party"
            elif [ $1 == 18 ]
            then
               echo "Return before mid night"
            else
               echo "you are not allowed"
            fi
            
       Scenario 2: 
       
            # we only want to perform an operation if the file is readable and has a size greater than zero.
            #!/bin/bash

            if [[ -r $1 ]] && [[ -s $1 ]]
            then
                echo "this is not empty"
            fi
         
       Scenario 3: 
       
            # Maybe we would like to perform something slightly different if the user is either centos or anand.
            #!/bin/bash
            USER=$1
            if [[ $USER == 'centos' ]] || [[ $USER == 'anand' ]]
            then
                echo "this is $USER"
            else
                echo "no user match"
            fi


----------------------------------------------------------------

## Check the String is palindrome or Not

               #!/bin/bash

               read name

               n=`echo $name|rev`
               #echo $n

               if [ $name == $n ]
               then
                       echo " The Styring is Palindrome "
               else
                       echo "this is not a palindrome"
               fi


## Arry Declaration with variables

         Scenario 1:
         
               #!/bin/bash

               array=( "anand" "reddy" "reddam" )
               for i in ${array[@]}
               do
                  echo  $i
               done
               
         Scenario 2:
         
              listVar="1 2 3"
              for j in $listVar
              do
                  echo "$j"
              done
              
         Scenario 3:
         
              list='"item 1" "item 2" "item 3"'
              for i in $list; do
                  echo $i
              done
              
              
              
