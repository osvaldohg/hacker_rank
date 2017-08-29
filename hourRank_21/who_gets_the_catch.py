#!/bin/python
#https://www.hackerrank.com/contests/hourrank-21/challenges/who-gets-the-catch
#by oz

import sys
import copy

def whoGetsTheCatch(n, x, X, V):
    # Complete this function
    
    if (n==1):
        return 0
    
    times=[]
    for i in xrange(n):
        d=abs(X[i]-x)
        speed=d/V[i]
        times.append(speed)
    
    min=times[0]
    index=0
    for i in xrange(1,n):
        if times[i]< min:
            min=times[i]
            index=i
        elif times[i]==min:
            index=-1
    
    return index
    
    

#  Return the index of the catcher who gets the catch, or -1 if no one gets the catch.
n, x = raw_input().strip().split(' ')
n, x = [int(n), int(x)]
X = map(int, raw_input().strip().split(' '))
V = map(int, raw_input().strip().split(' '))
result = whoGetsTheCatch(n, x, X, V)
print(result)
