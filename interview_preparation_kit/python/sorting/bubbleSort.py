#!/bin/python
# https://www.hackerrank.com/challenges/ctci-bubble-sort
# by oz 

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a,n):
    swaps=0
    for i in range(0,n):
        for j in range(0,n-1):
            if a[j]>a[j+1]:
                aux=a[j]
                a[j]=a[j+1]
                a[j+1]=aux
                swaps+=1
    
    print "Array is sorted in "+str(swaps)+" swaps."
    print "First Element: "+str(a[0])
    print "Last Element: "+str(a[-1])
    
    
if __name__ == '__main__':
    n = int(raw_input())

    a = map(int, raw_input().rstrip().split())

    countSwaps(a,n)
