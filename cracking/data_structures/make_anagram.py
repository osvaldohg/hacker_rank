# https://www.hackerrank.com/challenges/ctci-making-anagrams/problem
# by oz 

def number_needed(a, b):
    abc=[0 for x in xrange(26)]
    
    for i in a:
        apos=ord(i)-ord('a')
        abc[apos]+=1
    
    for i in b:
        bpos=ord(i)-ord('a')
        abc[bpos]-=1
    
    total=0    
    for j in abc:
        total+=abs(j)
        
    return total
            

a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)
