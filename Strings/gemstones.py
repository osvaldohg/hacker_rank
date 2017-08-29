#!/bin/python
# https://www.hackerrank.com/challenges/gem-stones/problem
# by oz


import sys

def  gemstones( rocks):
    inter=set(rocks[0])
    for i in range(1,len(rocks)):
        a=set(rocks[i])
        inter=inter.intersection(a)

    return len(inter)

n = int(raw_input().strip())
arr = []
arr_i = 0
for arr_i in xrange(n):
    arr_t = str(raw_input().strip())
    arr.append(arr_t)
result = gemstones(arr)
print(result)
