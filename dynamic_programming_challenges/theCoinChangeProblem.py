# https://www.hackerrank.com/challenges/coin-change/problem
# by oz

def getWays(n, c):
    # Complete this function
    vals = [0]*(n+1)
    vals[0] = 1
 
    for i in range(0,len(c)):
        for j in range(c[i],n+1):
            vals[j] += vals[j-c[i]]
            #print vals
 
    print vals[n]
    
n, m = raw_input().strip().split(' ')
n, m = [int(n), int(m)]
c = map(long, raw_input().strip().split(' '))
# Print the number of ways of making change for 'n' units using coins having the values given by 'c'
ways = getWays(n, c)