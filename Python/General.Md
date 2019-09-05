python
--------------

1. Installation of python
	
		https://www.python.org/downloads/

2. Pycahrm Installation

		http://www.jetbrains.com/pycharm/download/#section=windows

3. Python Concepts 

	a) Data Structures : 
	   ---------------

	    1. Numeric

	    	- Integer type

	    		Ex : a = 10

	    			$ Integer to float converter

	    				a = 10
	    			  	g = float(a)
						print (g)

	    	- Float type

	    	    Ex : b = 10.45

	    	    	$ Float to Integer converter
	    	    	    
	    	    	    e = 10.45
	    	    	    f = int(e)
						print (f) 

	    	- Complex type

	    		Ex : i = 7+8j
					 print (i)

	    	- long type

	    		Python no longer supporting the long type from 3.8 version on words .

	    		Ex:  d = 1000000786786*2009999999000009989

	    2. Lists

	    	Note :  List and array declaration should be same. But , the major difference is Array's can be declared with same data type but list can be any thing .

	    				# List diclaration

						list = ['anand','hari',200]
						print (list)

						# Update a List

						list[1] = "reddy"
						print (list)

						# Print the lenth of the list

						print (len(list))

						# Print the element of the list

						print (list[2])

						# Print the part of the list

						print (list[0:2])

						# concatinate of lists

						list2 = ['brush','bath','towel']
						print (list+list2)

						# Print list multiple times
						print (list2*2)

	    3. Tuples

	    	Note :  Tuples are also same like Lists but , these are immutable and declared with open and closed () .

	    			t1 = ("hello","trtey",786485)
					print (t1)


	    4. Strings 
	    
					    # String declaration

						a = " hello all this is anand !!"
						print (a)

						# string length\

						print (len(a))

						# Locate a character in string

						print (a.find('d'))
						print (a.index('d'))

						# Count the number of times the word repeated

						print (a.count('a'))

						# Print a part of string

						print (a[0:10])

						# Reverse a String

						print (a[::-1])

						# convert to upper case

						print (a.upper())

						# Convert to lower

						print (a.lower())

						# Concatinate a string

						print (a+'Hari')

						# print multiple times

						print (a*2)

	    5. Set

	    	Note : It is unordered collection of uniuqe items .

	    		t1 = ['anand','hari','h','h','g']
				g = set(t1)
				print (g)

	    6. Dictionary

	    		# Dictionary

				de = { 'name':'anand','roll':'1123','id':'67'}
				print (de['name'])
				print (de['id'])
				
	                # Deleate a record
			
			        dic = {'name':'anand','roll':571,'per':'70'}
				print(dic['name'])
				del dic['roll']
				print(dic)

			# Update a Record
			
				person['salary'] = 4342.4
				print(person) # Output: {'name': 'Jack', 'age': 36, 'salary': 4342.4}


	b. Python Operations


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


    c. Condition Statements in Python

    	1. if
    	2. elif
    	3. else

    	Ex :

    			a = 20
				b = 20
				if (a>b):
				    print('A is bigger')
				elif(a<b):
				    print('B is bigger')
				else:
				    print('both are equal')


	D. Loops in Python

		1. While

			string = "hello"
				a= 0
				while a < len(string):
				    print(a)
				    a=a+1

		2. For
			with list :

			mylist = [2,3,4,5,56,7,78]
				for a in mylist:
	   				 print(a)

	   		with dictonary:

	   			d = {'key':1,'key':2,'key':3}
				for a,b in d.items():
				    print(a)
				    print(b)


		3. Nested

			1.1 While :

					a = 0
					while (a<10):
					    print('the value of a',a)
					    a = a+1
					print('while executed successfully')


			3.1 Nested While

					i = 2
					while (i<100):
					    j = 2
					    while ( j<= (i/j) ):
					        if not (i%j): break
					        j=j+1
					    if (j>i/j): print(i,'is prime')
					    i=i+1

		4. Break,continue,pass
		



	E. Functions in Python

		A function is a block of organized , reusable code that is performed single releted action.

		1. Predefined function
		2. Userdefined function

			2.1 userdefined function


					def add(a,b):
					    c =(a+b)
					    return (c)
					p = add(2,7)
					print(p)


		    2.2 

		    		def greet(*names):
					   """This function greets all
					   the person in the names tuple."""

					   # names is a tuple with arguments
					   for name in names:
					       print("Hello",name)

					greet("Monica","Luke","Steve","John")



			
OOPS:
-----------------------------------------------------

1. Constructor 

		class Car():
		    def __init__(self,name,price,cc):
		        self.name = name
		        self.price = price
		        self.cc = cc

		honda = Car('city',30000,250)
		tata = Car('indica',50000,180)

		honda.many = 2019
		print(honda.cc)
		print(honda.__dict__)
		print(tata.__dict__)


2. Inheritence

		class Car():
		    def __init__(self,name,price,cc):
		        self.name = name
		        self.price = price
		        self.cc = cc

		    def price_inc(self):
		        self.price = self.price*1.15

		#honda = Car('City',5000,180)
		#print(honda.__dict__)
		#print(honda.price)
		#honda.price_inc()
		#print(honda.price)

		class childclass(Car):
		    def __init__(self,name,price,cc,mandate):
		        super.__init__(self,name,price,cc)
		        self.mandate = mandate

		honda = childclass('vitara',78978,320,2019)
		print(honda.__dict__)


--------------------------------------------------------------------------------------------

- Python range()
  
  	range() returns an immutable sequence of numbers between the given start integer to the stop integer.

  	print(range(1, 10)) # Output: range(1, 10)



		numbers = range(1, 6)

		print(list(numbers)) # Output: [1, 2, 3, 4, 5]
		print(tuple(numbers)) # Output: (1, 2, 3, 4, 5)
		print(set(numbers)) # Output: {1, 2, 3, 4, 5}

		# Output: {1: 99, 2: 99, 3: 99, 4: 99, 5: 99} 
		print(dict.fromkeys(numbers, 99))
		
		
	---  Operations on Numbers
	
	       # Equivalent to: numbers = range(1, 6)
		numbers1 = range(1, 6 , 1)
		print(list(numbers1)) # Output: [1, 2, 3, 4, 5]

		numbers2 = range(1, 6, 2)
		print(list(numbers2)) # Output: [1, 3, 5]

		numbers3 = range(5, 0, -1)
		print(list(numbers3)) # Output: [5, 4, 3, 2, 1]




# Multi Line statements

		a = 2+3+5+7+ \
		    8+9+ \
		    5+8
		print(a)

		b = (4+6+89+9+
		     7+8+9+9+
		     88+8+9)

		print(b)

		li = [ 'anand','reddy'
		       'jhfg','dfhgf','hjgfhf']

		print(li)




# Constants
			A constant is a type of variable whose value cannot be changed. It is helpful to think of constants as containers that hold information which cannot be changed later.

			constants are written in all capital letters and underscores separating the words.

				PI = 3.14
		    	GRAVITY = 9.8



# camelCase Notation

			  Use camelCase notation to declare a variable. It starts with lowercase letter. 
			 Ex: 
			  myName
			  myAge


# Print Options

			print(1,2,3,4,sep='#',end='&')
				# Output: 1#2#3#4&

# Output String Format

		    x = 5
			y = 10

			print('The value of x is {} and y is {}'.format(x,y))

		    ---- We can specify the order in which it is printed by using numbers (tuple index).
		 	     print('I love {0} and {1}'.format('mom','India'))


		    ---- We can even use keyword arguments to format the string.
		         print('Hello {name},{greetings}'.format(name='anand',greetings='morning'))


		    ---- We can even format strings like the old sprintf() style used in C programming language. We use the % operator to accomplish this.
		         a = 10
				 print('the a value is %3.2f' %a)



# What are lambda functions in Python?

			In Python, anonymous function is a function that is defined without a name.

			While normal functions are defined using the def keyword, in Python anonymous functions are defined using the lambda keyword.

			Hence, anonymous functions are also called lambda functions.







# File Handling

			employeeList = open("C://Users//ranaredd/Desktop/employeelist.txt",'r+')
			employeeList_copy = open("C://Users//ranaredd/Desktop/employeelist_copy.txt",'w')
			# employeeList.write("Hello Employees")


			for line in employeeList:
				token=line.split(' ')
				employeeList_copy.write(line+" wordCount:"+str(len(token)))




			# print(employeeList.read())

			# employeeList.write("\n He is a good learner")

			# print(employeeList.read())
			employeeList.close()


	-  File Operation to "With" for not closing the file explisitly
			

		with open("C://Users//ranaredd/Desktop/employeelist.txt",'r') as file:
			print(file.read())
		print(file.closed)


       -  Folder Handing
       
		import os
		# Get Present Working Directory
		print(os.getcwd())
		# Change Working Directory
		os.chdir('C:/Users/ranaredd/PycharmProjects/untitled')
		print(os.getcwd())
		# List of files in Present Working Directory
		print(os.listdir())
		# Remove a Folder
		os.rmdir('test')   
		print(os.listdir())
		# Craete a directory
		os.rmdir('test')
		print(os.listdir())
		
		
 # Time Modules
 
		import time

		start = time.time()

		now = time.gmtime()
		a = time.asctime(now)
		print(a)
		print(now)

		time.sleep(3)

		end = time.time()
		print(end-start)

