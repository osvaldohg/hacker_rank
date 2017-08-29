#https://www.hackerrank.com/challenges/ctci-fibonacci-numbers
#fibonacci numbers
#by oz


def fibonacci(n):
    # Write your code here.
    if n==0:
        return 0
    if n==1:
        return 1
    
    value=1
    prev=0
    total=0
    for i in xrange(1,n):
        total=prev+value
        prev=value
        value=total
            
    return total
        
n = int(raw_input())
print(fibonacci(n))
