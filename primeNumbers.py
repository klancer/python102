__author__ = 'yuy001'




print("input your number?")
num = int(raw_input())

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print("the %d is not prime" %num)
            print("the %d is divisible by %d" %(num, i))
            break
    else:
        print("the %d is prime" %num )
else:
    print("the %d is print" %num)


"""

# Python program to check if the input number is prime or not

# take input from the user
num = int(input("Enter a number: "))

# prime numbers are greater than 1
if num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")

# if input number is less than
# or equal to 1, it is not prime
else:
   print(num,"is not a prime number")
"""