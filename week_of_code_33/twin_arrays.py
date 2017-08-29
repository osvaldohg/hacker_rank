#!/bin/python
#https://www.hackerrank.com/contests/w33/challenges/twin-arrays
#by oz

import sys

def second(numbers,pos):
    if pos==0:
        return min(numbers[1:])
    
    if pos+1==len(numbers):
        return min(numbers[:pos])
    else:    
        amin=min(numbers[:pos])
        bmin=min(numbers[pos+1:])
        if amin <bmin:
            return amin
        else:
            return bmin
    
    
def twinArrays(ar1, ar2):
    # Complete this function
    min1=min(ar1)
    min2=min(ar2)
    pos1=ar1.index(min1)
    pos2=ar2.index(min2)
    
    if pos1 != pos2:
        return min1+min2
    else:
        aa=min1+second(ar2,pos2)
        bb=min2+second(ar1,pos1)
        #print aa,bb
        if aa>bb:
            return bb
        else:
            return aa
    

n = int(raw_input().strip())
ar1 = map(int, raw_input().strip().split(' '))
ar2 = map(int, raw_input().strip().split(' '))
result = twinArrays(ar1, ar2)
print(result)
