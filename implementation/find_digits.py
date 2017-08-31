#!/bin/python
# https://www.hackerrank.com/challenges/find-digits/problem
# by oz

import sys


t = int(raw_input().strip())

def checkDigits(number):
    lista=map(int,str(number))
    counter=0
    
    for i in lista:
        if i !=0 and number%i==0 :
            counter+=1
                
    return str(counter)
            
    

for a0 in xrange(t):
    n = int(raw_input().strip())
    #print "hola"
    print (checkDigits(n))