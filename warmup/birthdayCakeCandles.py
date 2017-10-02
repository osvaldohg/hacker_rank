#!/bin/python
# https://www.hackerrank.com/challenges/birthday-cake-candles/problem
# by oz

import sys

def birthdayCakeCandles(n, ar):
    # Complete this function
    maxv=0
    times=0
    for num in ar:
        if num > maxv:
            maxv=num
            times=1
        elif num==maxv:
            times+=1
            
    return times

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = birthdayCakeCandles(n, ar)
print(result)