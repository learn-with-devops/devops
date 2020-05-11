## Python

### Python OverView

    Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace.

    Features: 
    
    - Simple & Easy to learn
        - Open Source ( Under GPL Licenced)
        - Hight-Level Programming Language
        - InterPreted
        - Large Community
    
    - Portable & Extensible
        - Supports : Windows , Mac , Linux/Unix
        - Extensible: we can able to invoke Java,.net components to Python..C/C++ libraries also we can invoke ( cross language operations )
        
    - Web Development
        - Frameworks : Django , Flask , Pylons, Web2py
        
    - Artificial Intelligence
        - Analysing , Decision Making : like - Image recognation 
        
    - Computer Grphics
        - GUI , Desktop Applications , Game Development ( Libaries : jython , Tkinter ,Pygame )
        
    - Testing Frameworks
        - s/w testing to application  ( modules/tools : Selenium,Pytest )
        
    - BigData
        
    - Automation 
    
    - Data Science ( Numpy , Pandas )
    
    - Popularity / High Salary 
    
    
### Basic things

- variable
 
      Variables are containers for storing data values.
   
           # Variable Declaration

                    var = 'anand'
                    firstName = 'Anand'
                    first_Name = 'anand'
                    name2 = 'anand'
                    NAME = 'anand'

                    x, y, z = 10, 20, 30
                    print (x, y , z)

                    a =  b =  c = 'test'
                    print(a, b, c)
               
           # Illegal variable names:

                   2myvar = "John"
                   my-var = "John"
                   my var = "John"

- Keywords

        - Keywords are the reserved words in Python.
        - We cannot use a keyword as a variable name, function name or any other identifier. They are used to define the syntax and structure of the Python language.
        - There are 33 keywords in Python 3.7
        
        Example: 
        
            for, while , if , else, true, False, and , or, del , def , try, except, else, elseif, import , return , false
            
- Identifiers

        The identifier is only used to identify an entity uniquely in a program at the time of execution whereas, a variable is a name given to a memory location, that is used to hold a value. Variable is only a kind of identifier, other kinds of identifiers are function names, class names, structure names, etc.


- Indentation

        Python uses indentation to indicate a block of code.
 
- Comments

        Comments can be used to explain Python code.

        Comments can be used to make the code more readable.

        Comments can be used to prevent execution when testing code.
        
        Ex: 
        
        - Single line comments
        
            #This is a comment
            print("Hello, World!")
        
        - Multi-line
        
            """
            This is a comment
            written in
            more than just one line
            """
            print("Hello, World!") 

    

- Python Operatores


		1. Arithmetic
		   [ + , - , * , / , % , **(exponenent or square)]

		2. Comparision
		   [ == , != , > , < , >= , <= ]

		3. Membership
		   [ in , not in ]

		   3.1 in:
		    	a = 10
				list = [10,20,30,40,50]
				if (a in list):
				    print ('a in the present list')



			3.2 not in:
			 	a = 21
				list = [10,20,30,40,50]
				if (a not in list):
				    print ('a in not in the present list')

		4. Bitwise
		   [ & , | , ^ , ~ , << , >>]

		5. Logical Operators

			5.1 Logical AND

			    a = 10
				b = 20
				c = 0
				if ( a==10) and (b==a+10):
				    print ('logical and got passed')


			5.2 Logical OR

			    a = 10
				b = 20
				c = 0
				if ( a==10) or (b==a+30):
				    print ('logical and got passed')


			5.3  Logical NOT

				if (not c):
    			print ('condition true')


- Built-in Data Types
	
	  Variables can store data of different types, and different types can do different things.
	  
	       Numeric Types:    -- > int, float, complex, long( 3+ not support )
	       
	       		- Type Conversions : int() | float()
			
	       Sequence Types: 	 -- > list, tuple, range
	       
	       		- List : 
			
				names = ['Anand', 'Reddy', 'Reddam', 'Anand']
				names.count('Anand')  # number of times repeted
				names.index('Reddam') # Find a position of the value
				names.append(10) # Add a value at end
				names.insert(0, 'Srinu') # Insert a value in specific position
				names.extend([3, 'Hello', 'Anand']) # add multiple values at end
				names.remove('Anand') # Remove an Element
				names.pop(2) # default it remove last element. But we can specify the element you want.
				names.reverse() # Reverse a List
				names.sort() # Sort a List in Assending Order
				
	       Text Type:        -- > str
	       Mapping Type: 	 -- > dict
	       Set Types: 	 -- > set, frozenset
	       Boolean Type:     -- > bool
	       Binary Types: 	 -- > bytes, bytearray, memoryview
       
       
      ## Note: Frozen Set
     
              a = {1, 2, 5, 4, 3, 6, 4, 2}
              print(a)
              print (type(a))
              a.add(9)
              print(a)

              fs = frozenset(a)
              print(fs)
              fs.add(90)


### Built-In functions

- print()
- input()
- int(). --> For converting the value as Integer.
- float()  --> For converting the value as Float.
- type() --> For checking the type of variable.

### Differences:

- 'anand' & "anand"  --> for declare the data to a variable. Ex: name = "my name is 'anand'"
- '''anand''' | """anand"""
   ---> name = '''
            My name is Ananad
            From Anantpur
   '''
### Example: 

#### Print the current age ?

    birth_year = input('What is your birth year? ')
    print(type(birth_year))
    age = 2020 - int(birth_year)
    print('My current age is : ', age)

#### Print a string in required positions

    name = 'anandreddy'
    print(name[:]) --> copying the string
    print(name[0:2]) --> o/p: an
    print(name[1:-1])  --> o/p: nandredd
    
    
## Day-2 Topics ( FROM 37:40 to 1:11:30 )

### Formated Strings

Note: f'string support from 3.7 version onwords.
 
Ex: 

         first = 'anand'
         last = 'reddy'
         # Old Way of declaration to print "anand [reddy] is a coder"
         msg = first + ' [' + last + '] is a coder'
         print(msg)
         # Formatted String way to print "anand [reddy] is a coder"
         m1 = f'{first} [{last}] is a coder'
         print(m1)
         
 ### String Operations
 
         str = 'Hello all this is Anand'
         print(len(str))
         print(str.find('A'))
         print(str.index('A'))
         print(str.count('l'))
         print(str.replace('Anand', 'Reddy'))
         print(str[::-1]) # Reverse a string
         print(str[0:10])
         print (str[10:])
         
      ## In Operator with String
      
         print('Anand' in str). ##o/p: True|False

### Operator presidence

      Peranthasis()| Exponent(**) | Multiplication or division (*|/) | Addition or substraction (+|-)

### Round value

      print(round(2.9)) # o/p: 3
      print(abs(-2.9)) # o/p: 2.9
      
      ex: 
      import math
      print(math.ceil(2.9)) # o/p : 3
      print(math.floor(2.9)) # o/p: 2
      

### If-else condition

### Logical Operators in python

      AND => both conditions be valid
      OR  => atleast one should be valid
      NOT => converts to True if it is false and vice versa.
      
      Ex: 
      
      has_credit = True
      criminal_background = False
      
      if has_credit and not criminal_background:
         print("Eligible for loan")

## Day-3 (1:11:30 to 2:13:34 )

### If-else-if condition

      name = input('Enter the name : ')
      name_length = len(name)
      print (name_length)

      if name_length < 3:
          print('Name must be atleast 3 charecters')
      elif name_length > 50:
          print('Name is more than 50 charecters')
      else:
          print('Name looks good')
          
  
### LB's to Kilograms and Kg's to LB's

      weight = input('Enter the value :')
      print ('Weight = ', weight)
      type1 = input('(L)bs or (K)g: ')

      if type1 == 'L':
          lb = round(int(weight) * 2.210)
          print( f"you are {lb} kelograms" )
      elif type1 == 'K':
          kg = round(int(weight) / 2.210)
          print( f"you are {kg} lb's")
      else:
          print('Enter the proper input')
          
        

### Guess Program

      guess_count = 0
      guess_count_max = 3

      while guess_count < guess_count_max:
            guess = int(input("Enter your guess : "))
            if guess == 9:
                print('You Won !!')
                break
            guess_count += 1

      else:
          print('Sorry, You are wrong !! ')
          
 ## CAR stop/start/help program
 
      started = False
      while True:
          value = input('> ').lower()
          if value == 'help':
              print ('Start - To start a CAR')
              print ('Stop - To stop a CAR')
              print ('Quit - To exit')
          elif value == 'start':
              if started:
                  print('Car already started..!!')
              else:
                  started = True
                  print ('Car Started !!')
          elif value == 'stop':
              if not started:
                  print('Car already stopped')
              else:
                  started = False
                  print ('Car Stopped')
          elif value == 'quit':
              print('Exit a program')
              break
          else:
              print("I don't understand")
              
### Find a Big number in list

         numbers = [2, 9, 29, 92, 5]
         max = numbers[0]
         for i in numbers:
             if i > max:
                 max = i
         print(max)
         
### Print a unique values in list

         numbers = [2, 9, 9, 92, 5, 2, 9]
         list = []

         for i in numbers:
             if i not in list:
                 list.append(i)
         print (list)

### Iterate 2D list.

         list = [
             [1,2,3],
             [4,5,6],
             [7,8,9]
         ]
         for i in list:
             for j in i:
                 print(j)
                
## Un-Packing

   - It is a gretest mechanism for assigning the values of list  ot tuple directly like below.

   tu = ('anand', 'reddy', 571)
   x, y, z = tu
   print('x, y and z values are respectively ', x, y,z)


## Print the Emoji's with Dictionary ( For list out the emoji's use Control+Command+Space )

      inp = input("> ")
      word = inp.split(' ')
      print(word)

      emoji = {
          ':)': '😊',
          ':(': '😔'
      }

      ou = ""
      for wd in word:
          ou += emoji.get(wd, wd)
      print(ou)


## Functions

### Greetings with User-Defined Functions.

      def greetings(first_name, last_name):
          print(f'Hi {first_name} {last_name}!! Welcome to Cisco Systems India 🙂 ')

      greetings("Shashi", "Kumar")                           # Positional Arguments  : Order is a matter
      greetings(last_name="Reddy", first_name = "Anand " )   # Keyword_Arguments  : Order is not a matter 
      
      Note: 
            First preference is positional arguments and last preference is Key word arguments.
            
### try-Except Block

      try:
          age = int(input('Enter the Age: '))
          print(type(age))
          Income = 100000
          eligible = Income / age
          print('He is : ', eligible)
      except ValueError:
          print('Value should be an Integer')
      except ZeroDivisionError:
          print('Age should not be zero')
          
   

### Classes

      class HelloApp():
          def greetings(self):
              return "hello Anand"

          def sendoff(self):
              return "Bye"


      he = HelloApp()
      print(he.greetings())
      print(he.sendoff())


## Day-4

### Inheritence : 

       class Father:

           def land(self):
               print("Land Belong to all sons & Doughters")

           def liabilities(self):
               print("Sons need to the amount equally")

       class Son(Father):

           def commitments(self):
               print("Sons are responsible for commitments")

       class Daughters(Father):

           def funiral(self):
               print ("Dauthers need to take the funiral activities")


       son1 = Son()
       son1.commitments()
       son1.land()
       son1.liabilities()

       da1 = Daughters()
       da1.funiral()
       da1.liabilities()
       
       
## Modules

  1. max_value.py
  

         def max_value(number):
             max_number = number[0]

             for i in number:
                 if i > max_number:
                     max_number = i
             return max_number

 2. min_value.py
 

        def min_value(number):
           min_number = number[0]

           for i in number:
               if i < min_number:
                   min_number = i
           return min_number

  3. Main.py
  
         import max_value
         import min_value

         number = [20, 30, 18, 30, 66, 36]
         
         max = max_value.max_value(number)
         print (f'Max value in a List is {max}')

         min = min_value.min_value(number)
         print (f'Min value in a List is {min}')


## Random Module

         import random

         class Dice:

             def __init__(self):
                 pass

             def roll(self):
                     x = random.randint(1, 6)
                     y = random.randint(1, 6)
                     return f' ({x}, {y}) '

         input1 = Dice()
         print (input1.roll())
         
         
## Pathlib  (For show the files and folders of specific path )
 
       import pathlib

       # print (pathlib.Path.exists("ecommerce"))
       path = pathlib.Path("anand")


       # Create a Directory
       print (path.mkdir())

       # Remove a Directory
       print (path.rmdir())

       # Check the Directory exits
       print (path.exists())

       # Display all the files and folders 
       for file in path.glob('*'):
          print(file)
   
   
