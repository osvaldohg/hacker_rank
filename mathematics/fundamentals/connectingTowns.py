# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/connecting-towns/problem
# by oz

def solve(n, towns):
    res=1
    for t in towns:
        res*=t
    
    print res%1234567
    
nn=int(raw_input().strip())
#ans=
for t in range(nn):
    n=int(raw_input().strip())
    towns = map(int, raw_input().strip().split(' '))
    #print n,towns
    solve(n,towns)