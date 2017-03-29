#!/bin/python
#https://www.hackerrank.com/contests/w30/challenges/melodious-password
#by oz

import sys

n = int(raw_input().strip())

v=["a","e","i","o","u"]
c=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','u','v','w','x','z']
pairsA=[]
pairsB=[]


def print_lista(lista):
    for i in lista:
        print i
        
def duplas():
    for i in v:
        for j in c:
            pairsA.append(i+j)
    
    for i in c:
        for j in v:
            pairsB.append(i+j)
    
if n==1:
    print_lista(v) 
    print_lista(c)

elif n==2:
    duplas()
    print_lista(pairsA)
    print_lista(pairsB)

elif n==3:
    duplas()
    for i in v:
        for j in pairsA:
            print j+i
    
    for i in c:
        for j in pairsB:
            print j+i

elif n==4:
    duplas()
    for i in pairsA:
        for j in pairsA:
            print i+j
            
    for i in pairsB:
        for j in pairsB:
            print i+j

elif n==5:
    duplas()
    for i in pairsA:
        for j in pairsA:
            for k in v:
                print i+j+k
            
    for i in pairsB:
        for j in pairsB:
            for k in c:
                print i+j+k
                
elif n==6:
    duplas()
    for i in pairsA:
        for j in pairsA:
            for k in pairsA:
                print i+j+k
            
    for i in pairsB:
        for j in pairsB:
            for k in pairsB:
                print i+j+k
                  
