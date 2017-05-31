#!/bin/python

def max_sub(word):
    count=0
    max=0
    index=0
    
    sub=[]
    for i in range(0,len(word)):
        if word[i] in sub:
            if count > max:
                max=count
            count=0
            sub=[]
        else:
            count+=1
            sub.append(word[i])
        
    return str(max)    
        
        
print max_sub("booking.com")
    
   
    