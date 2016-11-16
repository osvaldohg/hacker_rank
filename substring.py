#stringtype:


def typeofstring(a,b):
    if set(a).issubset(set(b)):
        return "subset"
    
    if set(a).issuperset(set(b)):
        return "superset"
        
#main

print typeofstring("aaa","aba")


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


    

    
