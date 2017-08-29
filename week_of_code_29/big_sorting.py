#!/bin/python
# https://www.hackerrank.com/contests/w29/challenges/big-sorting/problem
# by oz

import sys


n = int(raw_input().strip())
unsorted = []
unsorted_i = 0
for unsorted_i in xrange(n):
    unsorted_t = int(raw_input().strip())
    unsorted.append(unsorted_t)
# your code goes here

#quicksort_oz
#quicksort using first element as pivot

counter=0
#print "quicksort"

def quicksort(arreglo,l,r):
    #print "quicksort oz"
    
    if l < r:
        p=partition(arreglo,l,r)
        quicksort(arreglo,l,p-1 )
        quicksort(arreglo,p+1,r)
    
def partition(arreglo,l,r):
    p=arreglo[l]
    
    i=l+1
    j=l+1
    global counter

    for x in range (j,r+1):
        
        counter+=1
        if arreglo[x] < p:
            #swap arreglo[j,i]
            tmp=arreglo[i]
            arreglo[i]=arreglo[x]
            arreglo[x]=tmp
            i+=1

    pivot=arreglo[l]
    arreglo[l]=arreglo[i-1]
    arreglo[i-1]=pivot
    return i-1

def readValues(path):
    fh=open(path,"r")
    lista=list()
    for line in fh:
        lista.append(int(line))

    return lista

#main

quicksort(unsorted,0,len(unsorted)-1)
for num in unsorted:
    print str(num)
#print unsorted

