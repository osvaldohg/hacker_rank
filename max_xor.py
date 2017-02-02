#!/bin/python
#https://www.hackerrank.com/challenges/maximizing-xor

# Complete the function below.


def  maxXor( l,  r):
    maxval=0
    for i in xrange(r-l):
        for j in range(l,r+1):
            tmp=l^j
            if tmp >maxval:
                maxval=tmp
        l+=1
    return maxval
    

_l = int(raw_input());


_r = int(raw_input());

res = maxXor(_l, _r);
print(res)

