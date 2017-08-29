#!/bin/python
# https://www.hackerrank.com/challenges/a-very-big-sum/problem
# by oz 

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

total=0
for number in arr:
    total=total+number

print total