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
    
    
## Day-2 Topics

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
