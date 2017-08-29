# Enter your code here. Read input from STDIN. Print output to STDOUT
#!/bin/python
# https://www.hackerrank.com/contests/w26/challenges/street-parade-1/problem
# by oz

import sys
minn=0
maxx=0
dist=0
sp=0

nn=int(raw_input().strip())
line=raw_input().strip()
points=list()

for a in line.split():
    points.append(int(a.strip()))

dist, minn, maxx=raw_input().split()
dist, minn, maxx=[int(dist), int(minn), int(maxx)]

upper=points[nn-1]+maxx
points.append(upper)

#print points

def verify(points,minn,maxx,dist,sp,i):
    #i=0
    pointer=sp
    #print "verifying"
    while i < len(points):
        #print "check"
        gap=abs(pointer-points[i])
        #print "gap",gap 
        if gap >= minn and gap <= maxx:
            dist=dist-gap
            #print "dist",dist
            if dist < 0:
                overlap=gap-abs(dist)
                if overlap >= minn and overlap <= maxx:
                    #print "a"
                    return True
            if dist==0:
                    #print "b"
                    return True
        else:
            #print "c"
            return False
        pointer=points[i]
        i+=1
        #print "d"
        
countMax=points[len(points)-1]-(points[0]-maxx)
value=False
sp=points[0]-maxx
count=0
#print "sp",sp
#print verify(points,minn,maxx,dist,0,2)
x=0
while not value and count <= countMax:
    #print "verify",dist,sp,x
    if sp in points:
        x=points.index(sp)+1
    value=verify(points,minn,maxx,dist,sp,x)
    if value:
        print sp

    sp+=1
    count+=1
