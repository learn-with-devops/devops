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
