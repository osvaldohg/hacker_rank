#!/bin/python
# https://www.hackerrank.com/challenges/encryption/problem
# by oz

import sys
import math

s = raw_input().strip()
size=len(s)
rows=0
cols=0

rows=int (math.floor(size**.5))
cols=int (math.ceil(size**.5))

if rows*cols <size:
    rows=int (math.ceil(size**.5))
    cols=int (math.ceil(size**.5))
    
#print rows,cols
res=""
for i in range(cols):
    for j in range(rows):
        val=(j*cols)+i
        #print val
        if val<size:
            res+=s[val]  
    res+=" "
    
print res
