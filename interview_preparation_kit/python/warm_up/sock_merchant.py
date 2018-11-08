#!/bin/python
#https://www.hackerrank.com/challenges/sock-merchant/problem
#by oz

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    numberOfPairs=0
    pairs={}
    
    for socket in ar:
        if socket in pairs:
            pairs[socket]+=1
        else:
            pairs[socket]=1
        
    for socket in pairs:
        numberOfPairs+=pairs[socket]/2
    
    
    return numberOfPairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    ar = map(int, raw_input().rstrip().split())

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
