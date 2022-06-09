## Python Programming interview questions

# reverse an Integer

        n = 198
        reverse = 0
        while n!=0:
            reverse = reverse*10 + n%10       
            n = (n//10)
        print(reverse) 

