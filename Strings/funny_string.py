# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/funny-string/problem
# by oz

t = int(raw_input().strip())
for a0 in xrange(t):
    n = raw_input().strip()
    start=1
    end=len(n)-2
    funny=True
    a=0
    b=0
    while start < len(n):
        a=abs(ord(n[start])-ord(n[start-1]))
        b=abs(ord(n[end])-ord(n[end+1]))
        
        if(a!=b):
            funny=False
            break
                
        start+=1
        end-=1
        #print start
    
    if funny:
        print "Funny"
    else:
        print "Not Funny"
        