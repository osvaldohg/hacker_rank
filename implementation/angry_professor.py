#!/bin/python
# https://www.hackerrank.com/challenges/angry-professor/problem
# by oz

import sys


t = int(raw_input().strip())

def isCanceled(students,total,atleast):
    ontime=0
    for i in range(0,total):
        if students[i]<=0:
            ontime+=1
        if ontime >=atleast:
            return "NO"
    
    return "YES"

for a0 in xrange(t):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = map(int,raw_input().strip().split(' '))
    
    print isCanceled(a,n,k) 
            
                  
        
    
           