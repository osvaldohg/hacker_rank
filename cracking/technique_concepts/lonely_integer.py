#!/bin/python
# https://www.hackerrank.com/challenges/ctci-lonely-integer/problem
# by oz

import sys

def lonely_integer(a):
    if len(a)==1:
        return a[0]
    
    x=a[0]
    for i in range(1,len(a)):
        x=x^a[i]
    
    return x

n = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))
print lonely_integer(a)