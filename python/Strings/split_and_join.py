# by oz
# https://www.hackerrank.com/challenges/python-string-split-and-join/problem

def split_and_join(line):
    # write your code here
    line2=line.strip().split()
    line2="-".join(line2)
    return line2
    