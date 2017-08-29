#!/bin/python
#https://www.hackerrank.com/challenges/anagram/problem
#by oz

import sys

def anagram(s):
    # Complete this function
    if len(s)%2==1:
        return -1
    d=dict()
    
    for i in range(0,len(s)/2):
        if s[i] in d:
            d[s[i]]=d[s[i]]+1
        else:
            d[s[i]]=1
    
    
    for i in s[(len(s)/2):]:
        if i in d:
            d[i]=d[i]-1
            
    result=0        
    
    for i in d.values():
        if i>= 0 :
            result+=i
        
    return result

q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    result = anagram(s)
    print(result)

