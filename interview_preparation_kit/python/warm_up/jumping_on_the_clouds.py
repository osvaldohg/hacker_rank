#!/bin/python
#https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem
#by oz

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jumps=0
    pos=0
    
    while pos!=len(c)-1:
        if pos+2 <=len(c)-1:
            if c[pos+2]==1:
                pos+=1
            else:
                pos+=2
            jumps+=1
        else:
            pos+=1
            jumps+=1
    
    
    return jumps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    c = map(int, raw_input().rstrip().split())

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
