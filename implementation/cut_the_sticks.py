#!/bin/python
# https://www.hackerrank.com/challenges/cut-the-sticks/problem
# by oz

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))


while len(arr)>0:
    cutsize=min(arr)
    print len(arr)
    i=0
    size=len(arr)
    while i < size: 
        arr[i]=arr[i]-cutsize
        if arr[i]==0:
            arr.pop(i)
            size=size-1
        else:
            i=i+1
       
        
        
        
        