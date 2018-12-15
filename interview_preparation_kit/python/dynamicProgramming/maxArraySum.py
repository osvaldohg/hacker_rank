#!/bin/python
# https://www.hackerrank.com/challenges/max-array-sum
# by oz

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    incl=0
    excl=0
    temp=0

    for i in range(0,len(arr)):
        temp=incl
        incl=max(incl,excl+arr[i])
        excl=temp

    return incl

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
