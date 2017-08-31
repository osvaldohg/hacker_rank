# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/sherlock-and-squares/problem
# by oz

t = int(raw_input().strip())
for a0 in xrange(t):
    a,b = raw_input().strip().split(' ')
    a,b = [int(a),int(b)]
    #print a,b
    squares=list()
    val=int(a**.5)
    
    while (val**2) <= b:
        if val**2 >=a and val**2<=b:
            squares.append(val)
        
        #print "val",val
        val+=1
        
    print len(squares)
    
    
    
