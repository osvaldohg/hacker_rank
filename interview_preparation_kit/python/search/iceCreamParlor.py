#!/bin/python
# https://www.hackerrank.com/challenges/ctci-ice-cream-parlor
# by oz 
import math
import os
import random
import re
import sys

# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    vals={}
    pos=1

    for val in cost:
        vals[val]=pos
        pos+=1

    current=1

    for val in cost:
        other=money-val
        if other in vals:
            if current != vals[other]:
                print current,vals[other]
                return
            
        current+=1

if __name__ == '__main__':
    t = int(raw_input())

    for t_itr in xrange(t):
        money = int(raw_input())

        n = int(raw_input())

        cost = map(int, raw_input().rstrip().split())

        whatFlavors(cost, money)
