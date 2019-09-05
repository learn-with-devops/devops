Exceptions & Error Handling : 
-----------------------------
		An exception is an error that happens during execution of a program. When that
		error occurs, Python generate an exception that can be handled, which avoids your
		program to crash.

		try:
		     p = open('csv_data.csv')
		     data = big_data
		except FileNotFoundError as e:
		    print(e)
		except Exception as e:
		    print(e)


#### Example with try , except, else and Finally block : 


		try:
		     p = open('csv_data.csv')
		    # data = big_data
		except FileNotFoundError as e:
		    print(e)
		except Exception as e:
		    print(e)
		else:
		    print(p.read())
		    p.close()
		finally:
		    print("Finally Executing Successfully")
	    
#### Raise Your own Exception :

		try:
		     p = open('csv_data.csv')
		     if p.name == 'csv_data.csv':
			 raise Exception
		except FileNotFoundError as e:
		    print(e)
		except Exception as e:
		    print('Manual Error')
		else:
		    print(p.read())
		    p.close()
		finally:
		    print("Finally Executing Successfully")
