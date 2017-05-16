#!/bin/python
#https://www.hackerrank.com/contests/w32/challenges/fight-the-monsters
#by oz

import sys

def getMaxMonsters(n, hit, t, h):
    # Complete this function
    a=sorted(h)
    counter=0
    for monster in a:
        #print monster
        if monster < hit:
            if t>0:
                counter+=1
                t-=1
            else:
                return counter
        else:    
            life=monster%hit
            if life==0:
                t=t-(monster/hit)
                if t>=0:
                    counter+=1
                else:
                    return counter
            else:
                t=t-(monster/hit)-1
                if t>=0:
                    counter+=1
                else:
                    return counter
    return counter        
        
n, hit, t = raw_input().strip().split(' ')
n, hit, t = [int(n), int(hit), int(t)]
h = map(int, raw_input().strip().split(' '))
result = getMaxMonsters(n, hit, t, h)
print(result)
