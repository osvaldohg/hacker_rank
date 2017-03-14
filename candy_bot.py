#!/bin/python
#https://www.hackerrank.com/contests/w30/challenges/candy-replenishing-robot
#by oz
import sys


n,t = raw_input().strip().split(' ')
n,t = [int(n),int(t)]
c = map(int, raw_input().strip().split(' '))
# your code goes here
added=0
nn=n
for i in xrange(t):
    if i < len(c):
        nn=nn-c[i]
        if nn <0:
            nn=0
        if nn < 5 and i < t-1:
            added+=n-nn
            #print added
            nn=n
print added
