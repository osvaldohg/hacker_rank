#!/bin/python
# https://www.hackerrank.com/challenges/utopian-tree/problem
# by oz

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    #print n
    i=0
    utopian=0
    while i <=n:
        if i%2 == 0:
            utopian=utopian+1
        else:
            utopian=utopian*2
        i+=1
    print utopian