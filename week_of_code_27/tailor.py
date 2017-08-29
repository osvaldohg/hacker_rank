#!/bin/python
# https://www.hackerrank.com/contests/w27/challenges/tailor-shop
# by oz

import sys


n,p = raw_input().strip().split(' ')
n,p = [int(n),int(p)]
a = map(int,raw_input().strip().split(' '))
# your code goes here
res=[]
last=0
stotal=0
for n in sorted(a):
    z= n/p
    x=z*p
    while x < n:
        z+=1
        x=z*p
    
    if z in res:
        z=last+1
        res.append(z)
        last+=1
        stotal+=z
    else:
        res.append(z)
        last=z
        stotal+=z
        
#print res
print stotal
