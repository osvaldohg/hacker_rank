#!/bin/python
#https://www.hackerrank.com/contests/w34/challenges/once-in-a-tram/problem
#by oz
import sys

def counts(num):
    snum=str(num)
    val=0
    for i in snum:
        val+=int(i)
    
    return val    

def add_zeros(val):
    totallen=3-len(val) 
    
    if len(val)!=0:
        return "0"*totallen+val
        
def onceInATram(x):
    # Complete this function
    number=str(x)
    left=int(number[0:3])
    right=int(number[3:])
    
    if right== 999:
        right=0
        left+=1
        
    else:
        right+=1
        
    leftc=counts(left)
    rightc=counts(right)
    
    while rightc!= leftc:
        if right == 999:
            right=0
            left+=1
            leftc=counts(left)
        right+=1
        rightc=counts(right)
    
    return str(left)+add_zeros(str(right))
    

if __name__ == "__main__":
    x = int(raw_input().strip())
    result = onceInATram(x)
    print result
