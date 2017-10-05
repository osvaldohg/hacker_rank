#!/bin/python
# https://www.hackerrank.com/challenges/grading/problem
# by oz
import sys

def solve(grades):
    # Complete this function
    ans=[]
    
    for num in grades:
        ans.append(cround(num))
        
    return ans
    
def cround(grade):
    if grade < 38:
        return grade
    
    num=grade/5
    if num*5 <grade:
        num+=1
        
    roundn=num*5
    
    if roundn-grade <3:
        return num*5
    else:
        return grade
    
n = int(raw_input().strip())
grades = []
grades_i = 0
for grades_i in xrange(n):
    grades_t = int(raw_input().strip())
    grades.append(grades_t)
result = solve(grades)
print "\n".join(map(str, result))


