#!/bin/python
# https://www.hackerrank.com/challenges/ctci-making-anagrams/problem
# by oz

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    dictA={}

    for letter in a:
        if letter in dictA:
            dictA[letter]+=1
        else:
            dictA[letter]=1
    
    for letter in b:
        if letter in dictA:
            dictA[letter]-=1
        else:
            dictA[letter]=-1
    
    total=0

    for letter in dictA:
        total+=abs(dictA[letter])

    return total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = raw_input()

    b = raw_input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
