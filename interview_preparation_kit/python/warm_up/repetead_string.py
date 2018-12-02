#!/bin/python
#https://www.hackerrank.com/challenges/repeated-string/problem
#by oz

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    ssize=len(s)
    count=0
    pcount=0
    fulltimes=n/ssize
    partime=n%ssize

    for i in range(0,ssize):
        if s[i] == 'a':
            count+=1
            if i <partime:
                pcount+=1
    
    return count*fulltimes + pcount
    
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    n = int(raw_input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
