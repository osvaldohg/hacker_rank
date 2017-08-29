#!/bin/python
# https://www.hackerrank.com/challenges/time-conversion/problem
# by oz

import sys


time = raw_input().strip()
ltime=time.split(":")
hour=int(ltime[0])

if "AM" in time:
    if hour==12:
        print "00"+time[2:8]
    else:
        print time[:-2]    
else:
    if hour==12:
        print time[:-2]
    else:
        hour=hour+12
        print str(hour)+time[2:8]
    
        
    

