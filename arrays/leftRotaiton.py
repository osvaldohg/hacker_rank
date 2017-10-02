#!/bin/python
# https://www.hackerrank.com/challenges/array-left-rotation/problem
# by oz
import sys

def leftRotation(a, d):
    # Complete this function
    offset=d%len(a)
    res=[]
    for i in range(0,len(a)):
        res.append(a[(i+offset)%len(a)])
        
    return res

if __name__ == "__main__":
    n, d = raw_input().strip().split(' ')
    n, d = [int(n), int(d)]
    a = map(int, raw_input().strip().split(' '))
    result = leftRotation(a, d)
    print " ".join(map(str, result))