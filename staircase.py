import sys
#by oz
#warm up in hacker rank

# Complete the function below.
def  StairCase(n):
    
    for i in xrange(1,n+1):
        diff=n-i
        print " "*diff+"#"*i
        
_n=int(raw_input());
StairCase(_n)
