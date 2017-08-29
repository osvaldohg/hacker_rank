#!/bin/python
# https://www.hackerrank.com/challenges/plus-minus/problem
# by oz

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

pos=0
neg=0
zero=0

for i in arr:
    if i == 0 : 
        zero=zero+1
    elif i < 0:
        neg=neg+1
    else:
        pos=pos+1
        
print pos/float(n)
print neg/float(n)
print zero/float(n)
