#!/bin/python
#https://www.hackerrank.com/contests/w32/challenges/duplication
#by oz

import sys

def duplication(lista,max,queries):
    # Complete this function
    chain=[0,1]
    while len(chain) < max:
        subchain=[]
        for i in chain:
            if i==0:
                subchain.append(1)
            else:
                subchain.append(0)
        chain+=subchain
        
    for num in lista:
        print chain[num]
    
    
q = int(raw_input().strip())
nums=[]
for a0 in xrange(q):
    x = int(raw_input().strip())
    nums.append(x)
    
duplication(nums,max(nums),q)   
