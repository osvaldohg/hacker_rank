#print "hk"

#!/bin/python

import sys

n,q = raw_input().strip().split(' ')
n,q = [int(n),int(q)]
angles=[]
max=0
for a0 in xrange(q):
    angle = int(raw_input().strip())
    angles.append(angle%360)
    if angle>=max:
        max=angle
    # your code goes here

#print angles
    
#hkd={1:1,2:2,3:3}
hkd=[0,1,2,3]
vals=[]
hkdd={1:1,2:2,3:3}

#def insertal(index,total,hkd):

def hk(val):
    if val ==1:
        return 1
    if val ==2:
        return 2
    if val==3:
        return 3
    #print "val",val
    for i in range(3,val):
        total=0
        h=3
        for j in range(1,4):
            total+=j*hkd[h]
            h-=1
        #print total
        #add to sized dict
        #hkd[i+1]=total
        hkd.append(total)
        hkd.pop(0)
        #print "i",i
        if i+1 in vals:
            hkdd[i+1]=total
        #print hkd
    return hkd[3]

def rotate(matrix,matrixo,n):
    count=0
    for layer in range(0,n/2):
        first=layer
        last=n-1-layer
        for i in range(first,last):
            offset=i-first
            #save top
            top=matrix[first][i]
            
            #left -> top
            if matrixo[first][i]!= matrix[last-offset][first]:
                count+=1
                
            matrix[first][i]=matrix[last-offset][first]
            
            #bottom -> left
            if matrixo[last-offset][first]!=matrix[last][last-offset]:
                count+=1
            matrix[last-offset][first]=matrix[last][last-offset]
            
            #right -> bottom
            if matrixo[last][last-offset]!=matrix[i][last]:
                count+=1
            matrix[last][last-offset]=matrix[i][last]
            
            #top -> right
            if matrixo[i][last]!=top:
                count+=1
            matrix[i][last]=top
            
    #print matrix
    #print count
    return count
        
#MAIN

#hk((n*n)**2)
#print hk(9)
#quit()
matrix=[]
matrixo=[]
for i in xrange(n):
    matrix.append([])
    matrixo.append([])
    for j in xrange(n):
        matrix[i].append(0)
        matrixo[i].append(0)

#print matrix

for i in xrange(n):
    for j in xrange(n):
        if ((i+1)*(j+1))**2 not in vals:
            vals.append(((i+1)*(j+1))**2)

#print vals            
hk((n*n)**2)
#print hkdd
            
for i in xrange(n):
    for j in xrange(n):
        #print ">>",((i+1)*(j+1))**2,hkd[((i+1)*(j+1))**2], hkd[7]
        if hkdd[((i+1)*(j+1))**2]%2==0:
            matrix[i][j]=0
            matrixo[i][j]=0
        else:
            matrix[i][j]=1
            matrixo[i][j]=1

#print "mat", matrix
rotations={360:0}
y=max%360
#print "max",y
if y==0 or y==270:
    x=rotate(matrix,matrixo,n)
    rotations[90]=x
    x=rotate(matrix,matrixo,n)
    rotations[180]=x
    x=rotate(matrix,matrixo,n)
    rotations[270]=x
elif y==180:
    x=rotate(matrix,matrixo,n)
    rotations[90]=x
    x=rotate(matrix,matrixo,n)
    rotations[180]=x
else:
    x=rotate(matrix,matrixo,n)
    rotations[90]=x
    
#print rotations

for ang in angles:
    if ang in rotations:
        print rotations[ang]
    
#rotate(matrix,matrixo,n)
