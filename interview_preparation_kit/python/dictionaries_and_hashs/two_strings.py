#!/bin/python
# https://www.hackerrank.com/challenges/two-strings/problem
# by oz

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    dicts1={}
    for letter in s1:
        if letter not in dicts1:
            dicts1[letter]=1

    for letter in s2:
        if letter in dicts1:
            return "YES"

    return "NO"
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(raw_input())

    for q_itr in xrange(q):
        s1 = raw_input()

        s2 = raw_input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
