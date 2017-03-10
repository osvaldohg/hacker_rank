#!/bin/python
#https://www.hackerrank.com/contests/womens-codesprint-3/challenges/ascii-flower
#by oz

import sys


r,c = raw_input().strip().split(' ')
r,c = [int(r),int(c)]
# your code goes here

line0="..O.."
line1="O.o.O"
line2="..O.."

for r_times in xrange(r*3):
    if r_times%3==0:
        print line0*c
    elif r_times%3==1:
        print line1*c
    elif r_times%3==2:
        print line2*c
