# Threading

Types of Multi Tasking : 

      - Process Based
              Multiple threads running on same OS simultaniously.
              Ex: 
                    Downloding , Listening the Songs , Playing a game etc..
              
      - Thread Based
              Single process consisting of separate tasks.
              Ex: 
                    A game of Fifa consisting of various threads ( like Backgroung Music , Video , Person moving , apposition moving )
                    

Multithreading in Python can be used at :

      -  Multiple tasks need to achieved.
      -  Tasks do not have interdependency.
                    


Create a Threads in Python in below ways : 

      - WithOut creating a Class
      - By Extending a Thread Class
      - WithOut extending a thread class


WithOut Craeting a Class :
--------------------------

            from threading import *
            print("hello",current_thread().getName())
            def task():
                for i in range(10):
                    print("Child program", current_thread().getName())
            t1 = Thread(target=task)
            t1.start()  # Start the thread
            t1.join()  # To run all the child processes at a time
            print("hello",current_thread().getName())
            
            
By Extending a Thread Class :
-----------------------------
