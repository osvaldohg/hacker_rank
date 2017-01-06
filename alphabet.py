# Enter your code here. Read input from STDIN. Print output to STDOUT
import string
n=int(raw_input())
#print size
abc=list(string.ascii_lowercase)
lchars=n+(n-1)
m=lchars+(lchars-1)
#print m, lchars

for i in xrange(lchars):
    line=""
    
    for j in range(1,lchars+1):
        pointer=abs(j-3)
        line=line+abc[pointer]
    
    print line
    
    
    

        ILVSS Dev is involved and looking at the issues
