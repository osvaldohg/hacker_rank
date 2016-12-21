#!/bin/python

import sys


n,p = raw_input().strip().split(' ')
n,p = [int(n),int(p)]
a = map(int,raw_input().strip().split(' '))
# your code goes here
b=sorted(a)
res=[]
last=0
stotal=0
for n in b:
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