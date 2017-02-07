#!/bin/python
#https://www.hackerrank.com/contests/hourrank-17/challenges/the-hurdle-race

import sys


n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
height = map(int, raw_input().strip().split(' '))
# your code goes here

max=0
for building in height:
    if building > max:
        max=building
        
if k >= max:
    print 0
else:
    print max-k
