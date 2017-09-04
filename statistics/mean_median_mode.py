# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/s10-basic-statistics/problem
# by oz

n=int(raw_input())
values=map(int, raw_input().strip().split())

values.sort()
avg=0.0
for number in values:
    avg+=number
    
avg=avg/n

median=0.0
if n%2==0:
    median=(values[n/2]+values[n/2-1])/2.0
else:
    median=values[n/2]
    
d={}

for i in values:
    if i in d:
        d[i]+=1
    else:
        d[i]=1

maxrep=max(d.values())
modes=[]

for i in values:
    if d[i]==maxrep:
        modes.append(i)

mode=modes[0]
print avg
print median
print mode