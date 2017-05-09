#!/bin/python
#https://www.hackerrank.com/contests/rookierank-3/challenges/comparing-times
#by oz
import sys

def timeCompare(t1, t2):
    # Complete this function
    #print t1,t2
    hour1=t1[:2]
    minute1=t1[3:5]
    am1=t1[5:]
    #print hour1,minute1,am1
    
    hour2=t2[:2]
    minute2=t2[3:5]
    am2=t2[5:]
    #print hour1,minute1,am1
    
    if am1 < am2:
        return "First"
    elif am1 == am2:
        #if am1 == "AM" and am2=="AM":
        if hour1=="12":
            hour1="00"
        if hour2=="12":
            hour2="00"
                
        if hour1 < hour2:
            return "First"
        elif hour1==hour2:
            if minute1 < minute2:
                return "First"
            else:
                return "Second"
        else:
            return "Second"
    else:
        return "Second"
    
q = int(raw_input().strip())
for a0 in xrange(q):
    t1, t2 = raw_input().strip().split(' ')
    t1, t2 = [str(t1), str(t2)]
    result = timeCompare(t1, t2)
    print(result)

