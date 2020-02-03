## OS Module 


Folder Handling with OS Module

	- Download the Module
          import os
          
	- Get Present Working Directory
	        print(os.getcwd())
          
	- Change Working Directory
	        os.chdir('C:/Users/ranaredd/PycharmProjects/untitled')
	        print(os.getcwd())
          
	- List of files in Present Working Directory
	        print(os.listdir())
          
	- Remove a Folder
	        os.rmdir('test')   
	        print(os.listdir())
          
	- Craete a directory
          os.mkdir('test')
          print(os.listdir())
