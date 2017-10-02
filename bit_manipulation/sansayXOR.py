# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/sansa-and-xor/problem
# by oz

nn=int(raw_input().strip())

for test in range(nn):
    n=int(raw_input().strip())
    arr = map(int, raw_input().strip().split(' '))
    total=0
    for i in range(n):
        val=(i+1)*(n-i)
        if val%2!=0:
            total^=arr[i]
    
    print total