#!/bin/python
# https://www.hackerrank.com/challenges/chocolate-feast/problem
# by oz

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n,c,m = raw_input().strip().split(' ')
    n,c,m = [int(n),int(c),int(m)]
    
    bars=n/c
    total=bars
    
    while (bars/m>0):
        total=total+(bars/m)
        bars=(bars/m)+(bars%m)
              
            
    
    print total
 