#!/bin/python
#An H-tree is a geometric shape that consists of a repeating pattern
# resembles the letter H.
#
#It can be constructed by starting with a line segment of arbitrary length,
#drawing two segments of the same length at right angles to the first through its endpoints,
#and continuing in the same vein, reducing (dividing) the length of the line segments 
#drawn at each stage by square 2
#
#Write a function drawHTree that constructs an H-tree, given its center (x and y coordinates),
#a starting length, and depth. Assume that the starting line is parallel to the X-axis.
#
#Use the function drawLine provided to implement your algorithm. In a production code, 
#a drawLine function would render a real line between two points. However, this is not a 
#real production environment, so to make things easier, implement drawLine such that it
#simply prints its arguments (the print format is left to your discretion).



def draw_line(x1,y1,x2,y2):
    #implement method
    print x1,y1,x2,y2
    pass

#x1,y1        x2,y1
#
#x1,y   x,y   x2,y
#
#x1,y2        x2,y2
    
def drawHTree(x,y,length,depth):
    if depth == 0:
        return 
    
    x1=x-length/2
    y1=y+length/2
    x2=x+length/2
    y2=y-length/2
    
    draw_line(x1,y1,x1,y2)
    draw_line(x1,y,x2,y)
    draw_line(x2,y1,x2,y2)
    ndepth=depth-1
    drawHTree(x1,y1,length**.5,ndepth)
    drawHTree(x1,y2,length**.5,ndepth)
    drawHTree(x2,y1,length**.5,ndepth)
    drawHTree(x2,y2,length**.5,ndepth)

#main

drawHTree(5,5,4,2)