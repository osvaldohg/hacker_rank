#!/bin/python
# https://www.hackerrank.com/challenges/alternating-characters/problem
# by oz

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    total=0

    for i in range(0,len(s)-1):
        if s[i]==s[i+1]:
            total+=1
    
    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(raw_input())

    for q_itr in xrange(q):
        s = raw_input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
