#!/bin/python
# https://www.hackerrank.com/challenges/balanced-brackets
# by oz

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    closed={"}":"{",
            ")":"(",
            "]":"["}
    
    stack=[]

    for i in s:
        if i not in closed:
            stack.append(i)
        else:
            if len(stack)==0:
                return "NO"
            if stack.pop() != closed[i]:
                return "NO"
    
    if len(stack)>0:
        return "NO"
    else:
        return "YES"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input())

    for t_itr in xrange(t):
        s = raw_input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
