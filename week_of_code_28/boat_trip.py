#!/bin/python
# https://www.hackerrank.com/contests/w28/challenges/boat-trip/problem
# by oz

import sys


n,c,m = raw_input().strip().split(' ')
n,c,m = [int(n),int(c),int(m)]
p = map(int, raw_input().strip().split(' '))

capacity=c*m
order=sorted(p,reverse=True)

for i in order:
    if capacity>= i:
        print "Yes"
        break
    else:
        print "No"
        break
        