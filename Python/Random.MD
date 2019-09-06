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
                          
                          
                  5. suffle()
                  
                              import random
                              list = [2,5,8,9,12]
                              random.shuffle(list)
                              print ("Printing shuffled list ", list)
                              
                  6. Print the list of values in 10 times
                              import random
                              list = [2,3,4]
                              value = random.choices(list, k=20)
                              print(value)

                  7. weights() for generating a perticular data based on our requirements
                              import random
                              list = [2,3,4]
                              value = random.choices(list, weights=[30,30,5], k=20)
                              print(value)
                              
                         Note: OutPut = [4, 2, 2, 3, 3, 2, 2, 3, 2, 2, 3, 3, 2, 3, 2, 2, 2, 3, 3, 2]
                         Here 2,3 getnerated a lot.Because, they have high weight and 4 generated rarely. Because they have less weight.
                         
                     
                         
                              
        - Random Floting Point Values
        
                 - uniform
                          
                              import random
                              value = random.uniform(1,30)
                              print(value)
                              
                              
         - Generate a Range of Numbers
         
                  - range()
                  
                              import random
                              li = list(range(1,30))
                              print(li)
                              
  

Generate a random Data from the list of general Data like below : 

                              anand Kumar
                              219-555-9087 
                              anandkumar@hcl.com

                              shashi naik
                              202-555-7424 
                              shashinaik@hcl.com

                              Hari Reddy
                              393-555-6882 
                              harireddy@hcl.com

Solution : 
                  import random
                  first_name = ['anand', 'shashi', 'mahesh','Hari','raghu']
                  last_name = ['Reddy','Kumar','Rebal','prasd','naik']
                  city = ['ban','pan','bage','mad','gul']

                  for num in range(10):
                      first = random.choice(first_name)
                      last = random.choice(last_name)
                      phone = f'{random.randint(100,400)}-555-{random.randint(6666,9999)}'
                      email = first.lower() + last.lower() + '@hcl.com'
                      print(f'{first} {last}\n{phone} \n{email}\n')
                              
