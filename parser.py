def parse(chain):
    openers={"(":")","[":"]","{":"}",}
    queue=list()
    
    #unbalanced
    if len(chain)%2==1:
        return False
        
    for i in chain:
        if i in openers.keys():
            queue.append(i)
            
        else:
            if len(queue)>0:
                if openers[queue.pop()] != i:
                    return False
            else:
                return False
    return True
    
#main
print "([{}])"
print parse("([{}])")
print parse("([{()}]")
