#!/bin/python
# https://www.hackerrank.com/challenges/simple-array-sum/problem
# by oz

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

total=0
for i in arr:
    total=total+i
    
print total