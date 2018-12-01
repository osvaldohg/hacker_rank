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
    count=0
    word=0
    size=len(s)%n

    for letter in s:
        if letter == 'a':
            word+=1

    for i in range(0,size):
        if letter == 'a':
            count+=1
            

    if n%len(s) == 0:
        count= word * (n/len(s))
    else:
        count=count + word * (n/len(s))

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    n = int(raw_input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
