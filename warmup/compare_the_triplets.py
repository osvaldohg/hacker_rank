#!/bin/python
# https://www.hackerrank.com/challenges/compare-the-triplets/problem
# by oz

import sys


a0,a1,a2 = raw_input().strip().split(' ')
a0,a1,a2 = [int(a0),int(a1),int(a2)]
b0,b1,b2 = raw_input().strip().split(' ')
b0,b1,b2 = [int(b0),int(b1),int(b2)]

acount=0
bcount=0

def check(a,b):
    global acount
    global bcount
    if a> b:
        acount+=1
    elif b>a:
        bcount+=1
        

check(a0,b0)
check(a1,b1)
check(a2,b2)

print acount,bcount