#!/bin/python
#https://www.hackerrank.com/challenges/2d-array
#by oz

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    maxval=-63

    for r in range(0,4):
        for c in range(0,4):
            value=arr[r][c]+arr[r][c+1]+arr[r][c+2]+arr[r+1][c+1]+arr[r+2][c]+arr[r+2][c+1]+arr[r+2][c+2]
            if value>maxval:
                maxval=value

    return maxval

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in xrange(6):
        arr.append(map(int, raw_input().rstrip().split()))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
