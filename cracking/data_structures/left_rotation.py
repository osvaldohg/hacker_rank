# https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem
# by oz

def array_left_rotation(a, n, k):
    index=k%n
    chain=a[index:]+a[:index]    
    
    return chain
   

n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, k);
print ' '.join(map(str,answer))
