#!/bin/python
#https://www.hackerrank.com/contests/womens-codesprint-3/challenges/the-birthday-bar
#by oz

import sys


n = int(raw_input().strip())
squares = map(int, raw_input().strip().split(' '))
d,m = raw_input().strip().split(' ')
d,m = [int(d),int(m)]
# your code goes here

last=len(squares)-m+1
count=0
for i in xrange(last):
    sum=0
    tmp=i
    for times in xrange(m):
        sum+=squares[tmp]
        tmp+=1
        
    if sum==d:
        count+=1
        
print count
