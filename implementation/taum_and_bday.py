#!/bin/python
# https://www.hackerrank.com/challenges/taum-and-bday/problem
# by oz

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    b,w = raw_input().strip().split(' ')
    b,w = [long(b),long(w)]
    x,y,z = raw_input().strip().split(' ')
    x,y,z = [long(x),long(y),long(z)]
    paint=0
    tb=0
    tw=0
    if z<x or z<y:
        if x <y:
            paint=x+z
            if paint > y:
                tw=w*y
            else:
                tw=w*paint
            tb=b*x
            
        else:
            paint=y+z
            if paint > x:
                tb=b*x
            else:
                tb=b*paint
            
            tw=w*y
        
    else:
        tb=b*x
        tw=w*y
        
    print tb+tw