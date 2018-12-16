#!/bin/python
# https://www.hackerrank.com/challenges/candies
# by oz
import math
import os
import random
import re
import sys

# Complete the candies function below.
def candies(n, arr):
    candies=[1 for x in xrange(n)]

    for i in range(1,n):
        if(arr[i] > arr[i-1]):
            candies[i] += candies[i-1];
    
    for i in range(n-2,-1,-1):
        if(arr[i] > arr[i+1] and candies[i] < candies[i+1]+1):
            candies[i] = candies[i+1]+1;
    
    result=0

    for candie in candies:
        result+=candie

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    arr = []

    for _ in xrange(n):
        arr_item = int(raw_input())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
