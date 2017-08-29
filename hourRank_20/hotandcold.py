#!/bin/python
#by oz
# https://www.hackerrank.com/contests/hourrank-20/challenges/hot-and-cold
import sys

def isSatisfiable(c1, c2, h1, h2):
    # Complete this function
    c=0
    h=0
    
    if c1>=c2:
        c=c1
    else:
        c=c2
    
    if h1<=h2:
        h=h1
    else:
        h=h2
    
    if c<=h:
        return "YES"
    else:
        return "NO"
    
    

# Return "YES" if all four conditions can be satisfied, and "NO" otherwise
c1, c2, h1, h2 = raw_input().strip().split(' ')
c1, c2, h1, h2 = [int(c1), int(c2), int(h1), int(h2)]
result = isSatisfiable(c1, c2, h1, h2)
print(result)
