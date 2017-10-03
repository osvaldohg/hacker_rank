#!/bin/python
# https://www.hackerrank.com/challenges/mini-max-sum/problem
# by oz
import sys


arr = map(int, raw_input().strip().split(' '))
minv=arr[0]
maxv=arr[0]
total=0

for num in arr:
    total+=num
    if num > maxv:
        maxv=num
    if num < minv:
        minv=num
#print total,minv,maxv      
print str(total-maxv) +" " +str(total-minv)
    