# Enter your code here. Read input from STDIN. Print output to STDOUT
#!/bin/python
# https://www.hackerrank.com/challenges/alternating-characters/problem
# by oz

import sys

t = int(raw_input().strip())
for a0 in xrange(t):
    m = raw_input().strip()
    pointer=0
    counter=0
    
    for i in range (1,len(m)):
        if (m[i]==m[pointer]):
            counter+=1
        else:
            pointer=i
            
    print counter
           
            
            
    
    

