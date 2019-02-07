#!/bin/python
# https://www.hackerrank.com/challenges/frequency-queries
# by oz

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the freqQuery function below.
def freqQuery(queries):
    ans=[]
    a = defaultdict(int) 
    b = defaultdict(int)

    for query in queries:
        data=query[1]
        if query[0]==1:
            b[a[data]] -= 1
            a[data]+=1
            b[a[data]] += 1
        elif query[0]==2:
            if data in a:
                b[a[data]] -= 1
                a[data] -= 1
                b[a[data]] += 1
            a[data]  = 0 if a[data] < 0 else a[data]

        elif query[0]==3:
            if data in b and b[data] > 0:
                ans.append(1)
            else:
                ans.append(0)
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(raw_input().strip())

    queries = []

    for _ in xrange(q):
        queries.append(map(int, raw_input().rstrip().split()))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
