#!/bin/python
#https://www.hackerrank.com/contests/rookierank-3/challenges/find-the-bug
#by oz

import sys

n = int(raw_input().strip())

y=0
x=0

for grid_i in xrange(n):
    grid_t = str(raw_input().strip())
    try:
        x=grid_t.index("X")
        break
    except ValueError:
        y+=1          
    
    
print "%d,%d" %(y,x)


