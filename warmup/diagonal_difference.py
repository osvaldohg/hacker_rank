#!/bin/python
# https://www.hackerrank.com/challenges/diagonal-difference/problem
# by oz

import sys


n = int(raw_input().strip())
a = []
for a_temp in xrange(n):
   a_temp = map(int,raw_input().strip().split(' '))
   a.append(a_temp)
    
#print a
diag1=0
diag2=0
j=n-1

for i in range(0,n):
    diag1=diag1+a[i][i]
    diag2=diag2+a[i][j]
    j=j-1

print abs(diag1 - diag2)
        
    
        
