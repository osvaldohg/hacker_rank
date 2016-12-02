# Enter your code here. Read input from STDIN. Print output to STDOUT
#!/bin/python
import sys
min=0
max=0
dist=0
sp=0

nn=int(raw_input().strip())
line=raw_input().strip()
points=list()

for a in line.split():
    points.append(int(a.strip()))

dist, min, max=raw_input().split()
dist, min, max=[int(dist), int(min), int(max)]

upper=points[nn-1]+max
lower=points[0]-max

points.append(upper)
points.insert(0,lower)

#print points
#print dist,min,max


def verify(points,min,max,dist,gaps,sp):
    for i in range(0,nn+1):
        gap=abs(sp-points[i+1])
        dist=dist-gap
        if dist ==0:
            print"a"
            return True
        elif dist <0:
            res=gap-abs(dist)
            print "res",res
            if res >=min and res <=max:
                print"b",res
                return True
            else:
                print"c"
                return False
            
        
#value=verify(points,min,max,dist,sp)
#print value

count=0
countMax=abs(points[0]-points[len(points)-1])
value=False
gaps=nn+1
pointergap=0
sp=points[0]

while not value and count <= countMax:
    value=verify(points,min,max,dist,gaps,sp)
    sp+=1
    count+=1 
    if sp>points[pointergap]:
        gaps+=1

        
    
