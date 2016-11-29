#!/bin/python

import sys
n = int(raw_input().strip())

#champion=[number,sum]
champion=[0,0]

for i in range(1,n+1):
    if n%i == 0:
        tmp=0
        number=str(n/i)
        for digit in number:
            tmp+=int(digit)
        
        if tmp > champion[1]:
            champion[0]=number
            champion[1]=tmp
                        
        if tmp == champion[1]:
            if int(number) < champion[0]:
                champion[0]=number
                champion[1]=tmp

print champion[0]
