## Python Programming interview questions

                        ## 0-------------------------0
                        # reverse an Integer

                                n = 198
                                reverse = 0
                                while n!=0:
                                    reverse = reverse*10 + n%10       
                                    n = (n//10)
                                print(reverse) 

                        ## 0-------------------------0
                        # Reverse a string
                        # Option-1
                        name = "anand"
                        # print(name[::-1])

                        # Option-2
                        def reverse(name):
                            str = ''
                            for i in name:
                                str = i + str
                            return str

                        print(reverse(name))

                        ## 0-------------------------0
                        # Prime Number
                        num = 96
                        signal = False

                        for i in range(2, num):
                            if (num % i) == 0:
                                signal = True
                                exit
                        if signal:
                            print("Not a Prime Number")
                        else:
                            print("Prime Number")
                            
                        ##0-----------------------0
                        ## Count the char 

                        ## Option-1
                        # str = "anand reddy !! how are you"

                        # for i in str:
                        #     count = 0
                        #     value = ''
                        #     for j in str:
                        #         if (i == j):
                        #             value = i
                        #             count = count + 1
                        #     print ('Char {} got repeted {} times'.format(set(value), count))

                        ## Option - 2 
                        # str = "Hello Boss"
                        # di = {}

                        # for i in str:
                        #     if i in di:
                        #         di[i] =+1
                        #     else:
                        #         di[i]=1
                        # print(di)

                        ### 0----------------------------0
                        ## FizzBuzz

                        # li = [40,77, 66, 22, 88, 95, 72, 15]

                        # for i in range(len(li)):
                        #     if li[i] % 3 == 0 and li[i] % 5 == 0:
                        #         li[i] = 'FizzBuzz'
                        #     elif li[i] % 3 == 0:
                        #         li[i] = 'Fizz'
                        #     elif li[i] % 5 == 0:
                        #         li[i] = 'Buzz'
                        # print(li)

                        ### 0----------------------------0
                        ## Print max number in a String / Array 

                        # arr = [10, 20, 489,8889]

                        # for i in range(len(arr)):
                        #     max = arr[0]
                        #     if arr[i] > max:
                        #         max = arr[i]
                        # print(max)
