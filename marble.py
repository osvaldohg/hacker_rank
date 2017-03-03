#!/bin/python
#https://www.hackerrank.com/contests/hourrank-18/challenges/wheres-the-marble
#where's the marble from hourrank18
#by oz

import sys


m,n = raw_input().strip().split(' ')
m,n = [int(m),int(n)]
ball=m
for a0 in xrange(n):
    a,b = raw_input().strip().split(' ')
    a,b = [int(a),int(b)]
    # your code goes here
    if ball==a:
        ball=b
    elif ball==b:
        ball=a
        
print ball
