# Enter your code here. Read input from STDIN. Print output to STDOUT
import string
n=int(raw_input())
#print size
abc=list(string.ascii_lowercase)

letters=n+(n-1)
lchars=letters+(letters-1)
count=1
reverse=False

def getchars(count,lchars):
    subchars=""
    #print "l",lchars
    res=(lchars-1)/2
    sider=n-1
    sreverse=False
    if count==1:
        return "-"*res+abc[n-1]+"-"*res
    
    for i in range(1,(count+1)+(count-1)):
        if i%2==0:
            subchars+="-"
        else:
            subchars+=abc[sider]
            if sider <= 0 or sreverse:
                sider+=1
                sreverse=True
            elif not sreverse:
                sider-=1
    
    if len(subchars)<lchars:
        res=(lchars-len(subchars))/2
        subchars="-"*res+subchars+"-"*res
    return subchars
        
for i in xrange(letters):
    cadena=""
    sidereverse=False
    sidecount=1
    chars=""
    
    print getchars(count,lchars)
       
    if count >= letters or reverse:
        count-=2
        reverse=True
    elif not reverse:
        count+=2
    
    
        
        





    

    
