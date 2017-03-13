#!/bin/python
#https://www.hackerrank.com/contests/womens-codesprint-3/challenges/hackathon-shirts
#by oz

import sys


q = int(raw_input().strip())
for a0 in xrange(q):
    n = int(raw_input().strip())
    sizes = map(int, raw_input().strip().split(' '))
    v = int(raw_input().strip())
    check=0
    ranges=[]
    for a1 in xrange(v):
        smallest,largest = raw_input().strip().split(' ')
        smallest,largest = [int(smallest),int(largest)]
        #print sizes
        i=0
        while i <len(sizes):
            #print "checking",sizes[i]
            if sizes[i]>= smallest and sizes[i]<=largest: 
                check+=1
                sizes.pop(i)
            else:
                i+=1    
                    
    print check      
