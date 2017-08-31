# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/palindrome-index/problem
# by oz

import string

t = int(raw_input().strip())
for a0 in xrange(t):
    nn = (raw_input().strip())
    n=list(nn)
    
    last=len(n)-1
    i = 0
    hold=0
    erase=-1
    failed=False
    
    while i < (len(n)/2):
        if n[i]==n[last]:
            i+=1
            last-=1
        else:
            if failed == False:
                hold=i
                erase=last
                last=last-1
                failed=True
            else:
                erase=hold
                i=i+1
    if failed:
        print erase
    else:
        print -1