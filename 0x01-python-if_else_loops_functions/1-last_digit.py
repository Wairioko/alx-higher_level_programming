#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if str(number)[-1] > 5:
    print("Last digit of {:d} is {str(number)[-1]} and is greater than 5".format(number))
elif str(number)[-1] < 6 & != 0:
    print("Last digit of {:d} is {str(number)[-1]} and is less than 6 and not 0".format(number))
else:
    print("Last digit of {:d} is {str(number)[-1]} and is 0".format(number))
    
