#!/bin/python
#by oz

def max_sub(word):
    if len(word)<2:
        return word
        
    init_max=0
    end_max=1
    init_current=0
    end_current=1
    
    while end_current < len(word):
        if word[end_current] in word[init_current:end_current]:
            if end_current-init_current > end_max-init_max:
                init_max=init_current
                end_max=end_current

            init_current=end_current
 
        end_current+=1
    
    if end_max==1:
        return word
    
    return word[init_max:end_max]

print max_sub("booking.com")
print max_sub("github.osvaldohg")
print max_sub("gmail.co")
print max_sub("g")

#results:
#oking.c
#github.osvald
#gmail.co
#g
    
   
    