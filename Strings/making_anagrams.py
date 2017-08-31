
# Enter your code here. Read input from STDIN. Print output to STDOUT
#!/bin/python
# https://www.hackerrank.com/challenges/making-anagrams/problem
# by oz

import sys
import string

a = raw_input().strip()
b = raw_input().strip()

#print a, b
d=dict()

for c in  a:
    if c not in d:
        d[c]=1
    else:
        d[c]=d[c]+1
       
    
    
for h in b:
    if h not in  d:
        d[h]=-1
    else:
        d[h]=d[h]-1
        
        
#print d
counter=0
for key in d:
    if d[key]!=0:
        counter+=abs(d[key])
        
print counter
  



    