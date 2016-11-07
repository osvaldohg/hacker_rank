def  gemstones( rocks):
    inter=set(rocks[0])
    for i in range(1,len(rocks)):
        a=set(rocks[i])
        inter=inter.intersection(a)      
        
    return len(inter)
    
    
 ##gemstones problem
