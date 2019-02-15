#!/bin/python
# https://www.hackerrank.com/challenges/largest-rectangle
# by oz

import math
import os
import random
import re
import sys

# Complete the largestRectangle function below.
def largestRectangle(h):
    stack=[]
    maxArea=0

    pos=0

    while pos<len(h):
        if (not stack) or (h[stack[-1]]<=h[pos]):
            stack.append(pos)
            pos+=1
        else:
            topStak=stack.pop()
            area=(h[topStak]*((pos-stack[-1]-1)if stack else pos))
        
            maxArea=max(maxArea,area)

    while stack:
        topStak=stack.pop()
        area=(h[topStak]*((pos-stack[-1]-1)if stack else pos))

        maxArea=max(maxArea,area)

    return maxArea 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    h = map(int, raw_input().rstrip().split())

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
