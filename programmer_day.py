#!/bin/python
#Day of the Programmer
#https://www.hackerrank.com/contests/w29/challenges/day-of-the-programmer
#by oz

import sys


year = int(raw_input().strip())
# your code goes here

def julian(y):
    if y%4==0:
        return "12.09."+str(y)
    else:
        return "13.09."+str(y)
    
def gregorian(y):
    if y % 400 == 0:
        return "12.09."+str(y)
    if y % 100 == 0:
        return "13.09."+str(y)
    if y % 4 == 0:
        return "12.09."+str(y)
    else:
        return "13.09."+str(y)

if year >= 1700 and year <= 1917:
    print julian(year)
elif year == 1918:
    print "26.08.1918"
elif year > 1918 and year <= 2700:
    print gregorian(year)
