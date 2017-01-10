# Enter your code here. Read input from STDIN. Print output to STDOUT
#Alphabet Rangoli
import string
n=int(raw_input())
abc=list(string.ascii_lowercase)

letters=n+(n-1)
lchars=letters+(letters-1)
count=1
reverse=False

def getchars(count,lchars,hcount):
    subchars=""
    sider=n-1
    sreverse=False
        
    for i in range(1,(count+1)+(count-1)):
        if i%2==0:
            subchars+="-"
        else:
            subchars+=abc[sider]
            if sider > hcount and not sreverse:
                sider-=1
            else:
                sider+=1
                sreverse=True
                
    if len(subchars)<lchars:
        res=(lchars-len(subchars))/2
        subchars="-"*res+subchars+"-"*res
    return subchars
        
for i in xrange(letters):
    hcount=abs(i-n+1)
    print getchars(count,lchars,hcount)
       
    if count >= letters or reverse:
        count-=2
        reverse=True
    elif not reverse:
        count+=2
    
