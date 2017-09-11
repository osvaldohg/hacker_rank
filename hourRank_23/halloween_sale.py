#!/bin/python
# https://www.hackerrank.com/contests/hourrank-23/challenges/halloween-sale/problem
# by oz

import sys

def howManyGames(p, d, m, s):
    # Return the number of games you can buy
    games=0
    money=p
    while money <= s:
        if (p-d) >= m:
            p-=d
        else:
            p=m
        
        money+=p
        games+=1
        
    return games
    

if __name__ == "__main__":
    p, d, m, s = raw_input().strip().split(' ')
    p, d, m, s = [int(p), int(d), int(m), int(s)]
    answer = howManyGames(p, d, m, s)
    print answer
