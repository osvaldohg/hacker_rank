#!/bin/python
#https://www.hackerrank.com/contests/world-codesprint-11/challenges/balanced-array
#by oz

import sys

def solve(nums,n):
    # Complete this function
    a=0
    b=0
    
    for x in xrange(n):
        if x < n/2:
            a+=nums[x]
        else:
            b+=nums[x]
            
    if a==b:
        return 0
    
    if a<b:
        return b-a
    else:
        return a-b

n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))
result = solve(a,n)
print(result)
