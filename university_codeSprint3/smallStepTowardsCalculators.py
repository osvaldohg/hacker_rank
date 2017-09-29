#!/bin/python
# https://www.hackerrank.com/contests/university-codesprint-3/challenges/a-small-step-toward-calculators
# by oz

import sys

def solve(opr):
    # Complete this function
    if opr[1]=="+":
        return int(opr[0])+int(opr[2])
    else:
        return int(opr[0])-int(opr[2])

if __name__ == "__main__":
    opr = raw_input().strip()
    result = solve(opr)
    print result
