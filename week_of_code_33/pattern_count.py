#!/bin/python
#https://www.hackerrank.com/contests/w33/challenges/pattern-count
#by oz


import sys

def patternCount(s):
    # Complete this function
    counter=0
    pattern=False
    zero=False
    
    for letter in s:
        if letter=="1" and pattern and zero:
            counter+=1
            zero=False
        elif letter=="1":
            pattern=True
            zero=False
        elif letter=="0":
            zero=True    
        elif letter!="0":
            pattern=False
            zero=False
            
    return counter

q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    result = patternCount(s)
    print(result)