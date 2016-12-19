#!/bin/python

import sys


n = int(raw_input().strip())
p = int(raw_input().strip())
# your code goes here

#print n,p

def pages(n,p):
    if n ==1 and p ==1:
        return 0
    
    if n==p:
        return 0
    
    if n==2:
        return 0
    
    if (n-p)==1:
        if n%2 == 0:
            return 1
        else:
            return 0
    
    
    
    s=p/2
    e=(n-p)/2
    
    if s <= e:
        return s
    else:
        return e

print pages(n,p)