# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/fibonacci-modified/problem
# by oz

a,b,n = raw_input().strip().split(' ')
a,b,n = [int(a),int(b),int(n)]

#print a,b,n
sum=0
for i in range(0,n-2):
    sum=b**2+a
    a=b
    b=sum
    
print sum