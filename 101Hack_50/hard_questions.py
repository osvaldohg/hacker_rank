#!/bin/python
#https://www.hackerrank.com/contests/101hack50/challenges/hard-questions
#by oz

import sys

def maxScoreOfVincent(n, s, t):
    # Complete this function
    counter=0
    for i in range(n):
        if s[i] != "." :
            if s[i] != t[i]:
                counter+=1
    
    return counter
                

#  Return the maximum score of Vincent.
n = int(raw_input().strip())
s = raw_input().strip()
t = raw_input().strip()
result = maxScoreOfVincent(n, s, t)
print(result)
