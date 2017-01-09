# Enter your code here. Read input from STDIN. Print output to STDOUT
import string
n=int(raw_input())
#print size
abc=list(string.ascii_lowercase)

letters=n+(n-1)
lchars=letters+(letters-1)
count=1
reverse=False
for i in xrange(letters):
    cadena=""
    for j in xrange(lchars):
        cadena+="a"
    
    print cadena,count
    
    if count >= letters or reverse:
        count-=2
        reverse=True
    elif not reverse:
        count+=2
    
    
        
        





    
