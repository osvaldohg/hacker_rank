#!/bin/python
#https://www.hackerrank.com/contests/w30/challenges/find-the-minimum-number
#by oz

import sys


n = int(raw_input().strip())

if n==2:
    print "min(int, int)"
else:
    cadena="min(int, "
    cadena=cadena+"min(int, "*(n-2)
    
    cadena+="int"
    cadena=cadena+")"*(n-1)
    
    print cadena
 
