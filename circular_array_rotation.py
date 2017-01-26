#!/bin/python
#Circular Array Rotation 

import sys


n,k,q = raw_input().strip().split(' ')
n,k,q = [int(n),int(k),int(q)]
a = map(int,raw_input().strip().split(' '))
res=[]
for a0 in xrange(q):
    m = int(raw_input().strip())
    value=m-(k%n)
    res.append(a[value])
    
for i in res:
    print i
