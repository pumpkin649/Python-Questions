#!/bin/python3

import math
import os
import random
import re
import sys



#
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