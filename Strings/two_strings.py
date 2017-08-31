# Enter your code here. Read input from STDIN. Print output to STDOUT
#!/bin/python
# https://www.hackerrank.com/challenges/two-strings/problem
# by oz

import sys

def calculate(a,b):
    status=False
    dictio=dict()    
    for count in range(0,len(b)):
        if b[count] not in dictio:
            dictio[b[count]]=1
    
    for i in range(0,len(a)):
        if a[i] in dictio:
            return "YES"
        
    return "NO"
   
        

t = int(raw_input().strip())
for i in range(0,t):
    a=(raw_input().strip())
    b=(raw_input().strip())
    
    if(len(a)>len(b)):
        print calculate(b,a)
    else:
        print calculate(a,b)
    
            
        
    
    
    

