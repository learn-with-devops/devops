## Day-1 Topics ( From: 0.0 to 37:40 )

### Terminalogies
- variable
- Expression

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
            
