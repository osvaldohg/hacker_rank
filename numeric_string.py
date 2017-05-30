#!/bin/python
#https://www.hackerrank.com/contests/world-codesprint-11/challenges/numeric-string
#by oz

import sys

def getMagicNumber(s, k, b, m):
    # Complete this function
    #s string
    #k substring length
    #b base
    #m module
    
    dictionary={}
    converted={}
    for i in range(0,len(s)-k+1):
        sub=s[i:i+k]
        
        if sub in dictionary:
            dictionary[sub]=dictionary[sub]+1
        else:
            dictionary[sub]=1
        
    total=0  
    todec=0
    for val in dictionary:
        #print val
        todec=int(val,b)
        total+=(todec%m)*dictionary[val]
    
    return total

s = raw_input().strip()
k, b, m = raw_input().strip().split(' ')
k, b, m = [int(k), int(b), int(m)]
result = getMagicNumber(s, k, b, m)
print(result)
