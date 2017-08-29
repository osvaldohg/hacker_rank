#!/bin/python
#by oz
#https://www.hackerrank.com/contests/w31/challenges/accurate-sorting

import sys

def swapping(a):
    for i in xrange(0,len(a)):
        if abs(a[i]-i)>=2:
            return "No"
        
    return "Yes"    

q = int(raw_input().strip())
for a0 in xrange(q):
    n = int(raw_input().strip())
    a = map(int, raw_input().strip().split(' '))
    # Write Your Code Here
    print swapping(a)

