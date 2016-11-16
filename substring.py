#stringtype:
       
def types(a,b):
    if len(a) == len(b):
        if a == b:
            return "equal"
    
    if len(a) < len(b):
        return checker(a,b,"sublist")        
    else:
        return checker(b,a,"superlist")
        
def checker(small,big,message):
    i=0
    j=0
    match=False
    while j < len(big):
        if i < len(small):
            if big[j]==small[i]:
                i+=1
                match=True
            else:
                i=0
                match=False
        else:
            return message
        j+=1
        
    if match:
        return message
    else:
        return "neither"    
        
        
#main


#subset all a in b
#superset all b in a
#main

A=[1,2,3]
B=[1,2,3,4,5]
#sublist

C=[1,2,3]
D=[1,2,3]
#"equal"

E=[1,2,3,4,5]
F=[2,3,4]
#superlist

G=[1,2,4]
H=[1,2,3,4,5]
#neither

I=[3,4,5]
J=[6,7,8]
#neither

K=[2,3,4]
L=[1,2,3,4]
#sublist

M=[1,2,3]
N=[1,2,0,1,2,3]
#sublist

print types(A,B)
print types(C,D)
print types(E,F)
print types(G,H)
print types(I,J)
print types(K,L)
print types(M,N)

    

    
