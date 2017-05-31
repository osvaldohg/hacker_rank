#!/bin/python
#by oz

def check_next(first,letter):
    #if len(first)==1:
    #    print "lol"
    #    return 0
    try:
        id=first.index(letter)
        return id 
    except ValueError:
        return -1
    


def sort_names(names):
    print "sorting"
    first=[]
    last=[]

    for name in names:
        first.append(name[0].lower())
        last.append(name[-1].lower())

    sortednames=[]    
    
    for i in range(0,len(first)):
        if first[i] not in last:
            sortednames.append(names[i])
            first.pop(i)
            last.pop(i)
            names.pop(i)
            break

    tmp=[]
    print sortednames
    print first
    print last
    print names

    #for i in range(0,len(names)):
    i=0
    na=0
    while na<7:
        if len(first)==1:
            sortednames.append(names.pop())
            return sortednames

        tmp=[]
        lastletter=sortednames[-1][-1]
        print lastletter
        print sortednames
        print first
        print last
        print names
        print "this is i ",i
        
        for i in range(0,len(first)):
            if lastletter == first[i]:
                tmp.append(names[i])
                print tmp

        for j in range(0,len(tmp)):
            val=check_next(first,tmp[j][-1])
            if val!=-1:
                print "holla ",tmp[j]
                sortednames.append(tmp[j])
                first.pop(first.index(tmp[j][0].lower()))
                last.pop(first.index(tmp[j][-1]))
                print "mmmm",names
                names.pop(names.index(tmp[j]))

        na+=1

    return sortednames 


n=["Raymond","Nora","Daniel","Louie","Peter","Esteban"]

print sort_names(n)
