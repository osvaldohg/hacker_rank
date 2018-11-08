#!/bin/python
#https://www.hackerrank.com/challenges/counting-valleys
#by oz

import math
import os
import random
import re
import sys


# Complete the countingValleys function below.
def countingValleys(n, s):
    level=0
    valley=0
    enter=False
    
    for direction in s:
        if direction == "U":
            level+=1
        else:
            level-=1
        
        if level<0:
            enter=True
        elif level==0 and enter:
            valley+=1
            enter=False      
        
    
    return valley
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    s = raw_input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
