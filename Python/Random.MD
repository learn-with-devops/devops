## Random Module in Python

Following are the list of common operations that we are going to cover in this article.

      Generate random numbers for various distributions including integer and floats.
      Random Sampling and choose elements from the population.
      Functions of the random module.
      Shuffle the sequence data. Seed the random generator.
      Generate random strings and password.
      Cryptographically secure random generator using secrets module. Generate secure tokens, security keys, and URL
      How to set the state of a random generator.
      Use numpy.random to generate random arrays.
      Use the UUID module to generate unique IDs
      
Operations : 

      - Print a Random number
      
                import random
                print("Printing random number using random.random()")
                print(random.random())
                
      - To generate random integers, we can use the following two functions.

                1. randint()
                          import random
                          value = random.randint(1, 20)
                          print(value)
                          
                2. randrange()
                  
                          print("Printing random integer ", randrange(0, 10, 2))
                          
                3. choice()
                   
                   Use the random.choice method to pick a random element from the sequence. 
                   Here sequence can be list or string. This method returns a single item from the sequence.
                   
                          import random
                          list = ['Anand','Reddy','Shashi','Kumar']
                          value = random.choice(list)
                          print('Hello ' + value)
                          
                 4. sample()
                    Sample method returns a list of unique elements chosen from the population. Count of the total elements depends on the size of k.
                    The population can be the list, set or any sequence.
                   
                          import random
                          list = [2,4,5,6,8,10]
                          print(random.sample(list,2))
