#!/bin/python
#https://www.hackerrank.com/challenges/new-year-chaos
#by oz

def bubblesort(lista):
    count=0
    bribe=False
    for x in xrange(len(lista)):
        if lista[x]-x>3:
            return "Too chaotic"
            
    for i in xrange(0,len(lista)-1):
        for j in xrange(0,len(lista)-1):
                                      
            if lista[j]>lista[j+1]:
                tmp=lista[j]
                lista[j]=lista[j+1]
                lista[j+1]=tmp
                count+=1
                bribe=True
              
        if bribe:
            bribe=False
        else:
            break
    
    return count

T = int(raw_input().strip())
numbers=[]
for a0 in xrange(T):
    n = int(raw_input().strip())
    q = map(int,raw_input().strip().split(' '))
    print bubblesort(q)
