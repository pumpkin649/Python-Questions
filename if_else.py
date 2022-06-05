#!/bin/python3

import math
import os
import random
import re
import sys



#1
# Complete the 'calculateGrade' function below.
#
# The function accepts INTEGER grade as parameter.
#

def calculateGrade(score):
    if score>=93:
        grade='A'
    elif score>=84 and score<=92:
        grade='B'
    elif score >=74 and score<=83:
        grade='C'
    elif score >=65 and score<=73:
        grade='D'
    else:
        grade='F'

    print(grade)
    
if __name__ == '__main__':
    score = int(input().strip()) 
    calculateGrade(score)


#2
#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'playGolf' function below.
#
# The function accepts following parameters:
#  1. STRING outlook
#  2. STRING windy
#  3. STRING humidity
#

def playGolf(outlook, windy, humidity):
    # Write your code here
    
    if outlook=="rainy" and windy=="True":
        print("play")
    elif outlook=="overcast":
        print("play") 
    elif outlook=="sunny" and humidity=="normal":
        print("play")
    else:
        print("don't play")

if __name__ == '__main__':
    
    outlook = input()

    windy = input()

    humidity = input()

    playGolf(outlook, windy, humidity)


#3
#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'largestNum' function below.
#
# The function accepts following parameters:
#  1. INTEGER num1
#  2. INTEGER num2
#  3. INTEGER num3
#

def largestNum(num1, num2, num3):
    if num1>=num2 and num1>=num3:
        print(num1)
    elif num2>=num1 and num2>=num3:
        print(num2)
    elif num3>=num1 and num3>=num1:
        print(num3)

if __name__ == '__main__':
    
    num1 = int(input().strip())

    num2 = int(input().strip())

    num3 = int(input().strip())

    largestNum(num1, num2, num3)
