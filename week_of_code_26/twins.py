# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/contests/w26/challenges/twins/problem
# by oz

#!/bin/python

import sys
import math

nn,mm = raw_input().split()
nn,mm = [int(nn),int(mm)]
#print n,m
prime_list=[]
def calculate(n,m):
    counter=0
    
    top=int(math.sqrt(m))

    for i in range(n,m+1):
        prime=True
        x=2
        while x < i and x <= top:
            
            if i%x == 0:
                prime=False
                break
            x+=1
        
        if i not in prime_list and prime and i!=1:
            prime_list.append(i)
            
    
    #return len(prime_list)        
        
def all(n,m):
    prime_list2=[3]
    counter=0
    top=int(math.sqrt(m)) 

    if n%2==0:
        n+=1
    for i in range(n,m+1,2):
        prime=True
        x=0
        while x < len(prime_list) and prime_list[x] < i and prime_list[x] <= top:
            
            if i%prime_list[x] == 0:
                prime=False
                break
            x+=1
        
        if i not in prime_list2 and prime and i!=1:
            prime_list2.append(i)
            if len(prime_list2)==2:
                res=prime_list2[1]-prime_list2[0]
                #print "comparing",prime_list2[0],prime_list2[1]
                if res == abs(2):
                    counter+=1
                    #print "comparing",prime_list2[0],prime_list2[1]
            
                prime_list2.remove(prime_list2[0])        
    
    return counter



calculate(1,31622)
#print len(prime_list)
print all(nn,mm)
