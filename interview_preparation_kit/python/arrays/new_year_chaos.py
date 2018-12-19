#!/bin/python
# https://www.hackerrank.com/challenges/new-year-chaos
# by oz

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    count=0
    
    for i in range(len(q)-1,-1,-1):
        if q[i]!=i+1:
            if (i-1)>=0 and q[i-1]==i+1:
                count+=1
                temp=q[i]
                q[i]=q[i-1]
                q[i-1]=temp
            elif (i-2)>=0 and q[i-2]==i+1:
                count+=2
                q[i-2]=q[i-1]
                q[i-1]=q[i]
                q[i]=i+1
            else:
                return "Too chaotic"

    return count

if __name__ == '__main__':
    t = int(raw_input())

    for t_itr in xrange(t):
        n = int(raw_input())

        q = map(int, raw_input().rstrip().split())

        print minimumBribes(q)
