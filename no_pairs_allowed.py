#!/bin/python
#by oz

import math
import os
import random
import re
import sys


#
# Complete the 'minimalOperations' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY words as parameter.
#
def minimalOperations(words):
    # Write your code here
    ans=[]
    for word in words:
        start=word[0]
        letterCount=1
        count=0
        for letter in word[1:]:
            if start==letter:
                letterCount+=1
            else:
                count+=letterCount/2
                letterCount=1
                start=letter
        count+=letterCount/2
        ans.append(count)
    return ans

print minimalOperations(["ab","aab","abb","abab","abaaaba"])
print minimalOperations(["aab"])