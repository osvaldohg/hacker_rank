#!/bin/python
# https://www.hackerrank.com/challenges/sherlock-and-valid-string
# by oz
import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
    flag=False
    max_val=-1

    alpha=[0 for x in range(0,26)]

    for letter in s:
         alpha[ord(letter)-ord('a')]+=1

    print alpha

    for val in alpha:
        if val !=0:
            if val != max_val:
                if max_val ==-1:
                    max_val=val
                else:
                    if abs(val-max_val)>1 and val!=1:
                        return "NO"
                    else:
                        if flag:
                            return "NO"
                        else:
                            flag=True
                
    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
