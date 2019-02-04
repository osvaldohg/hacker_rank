#!/bin/python
# https://www.hackerrank.com/challenges/special-palindrome-again
# by oz

import math
import os
import random
import re
import sys

def sameCount(n,s):
    subtotal=0
    count=1
    for i in range(1,n):
        if s[i]==s[i-1]:
            count+=1
            subtotal+=count-1
        else:
            count=1
    return subtotal

def palindromeCount(n,s):
    offset=1
    count=0

    for i in range(1,n-1):
        offset=1
        while (i-offset)>= 0 and (i+offset)<n:
            c=s[i+1]
            if s[i-offset] == c and c== s[i+offset] and s[i]!=s[i-offset]:
                count+=1
            else:
                break
            offset+=1

    return count

# Complete the substrCount function below.
def substrCount(n, s):
    return sameCount(n,s)+palindromeCount(n,s)+n

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    s = raw_input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
