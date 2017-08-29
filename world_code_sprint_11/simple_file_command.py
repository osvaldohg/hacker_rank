#!/bin/python
#https://www.hackerrank.com/contests/world-codesprint-11/challenges/simple-file-commands
#by oz

import sys

q = int(raw_input().strip())

crt="crt"
dl="del"
rnm="rnm"

dict={}

def cmd_crt(c,quiet):
    #
    pointer=0
    if c[1] in dict:
        #dict[c[1]].append(1)
        #pointer=0
        
        try :
            pointer=dict[c[1]].index(0)
            dict[c[1]][pointer]=1
        except ValueError:
            pointer=len(dict[c[1]])
            dict[c[1]].append(1)
        
        if pointer==0:
            if not quiet:
                print "+",c[1]
        else:
            if not quiet:
                print "+",c[1]+"("+str(pointer)+")"
        
    else:
        dict[c[1]]=[1]
        if not quiet:
            print "+",c[1]
    
    return pointer
    #print dict
def cmd_dl(c,quiet):
    #
    id=0
    shortname=c[1][:len(c[1])-3]
    if "(" in c[1]:
        id=int(c[1][len(c[1])-2:len(c[1])-1:])
        #print id
        dict[shortname][id]=0
    else:
        dict[c[1]][id]=0
        
    if not quiet:
        print "-",c[1]   
        
        
    
def cmd_rnm(c):
    #
    id=0
    param1=""
    param2=""
    
    if "(" in c[1]:
        param1=c[1][:len(c[1])-3]
    else:
        param1=c[1]
    
    if "(" in c[2]:
        param2=c[2][:len(c[2])-3]
    else:
        param2=c[2]
        
    
    cmd=["crt",c[2]]
    val=cmd_crt(cmd,True)
    
    cmd2=["del",c[1]]
    cmd_dl(cmd2,True)
    
    name=""
    if val!=0:
        name=param2+"("+str(val)+")"
    else:
        name=param2
        
    print "r",c[1],"-> "+name

# Process each command
for a0 in xrange(q):
    # Read the first string denoting the command type
    command = raw_input().strip().split()
    # Write additional code to read the command's file name(s) and process the command
    # Print the output string appropriate to the command
    #print command
    #print dict
    if command[0]==crt:
        cmd_crt(command,False) 
    elif command[0]==dl:
        cmd_dl(command,False)
    elif command[0]==rnm:
        cmd_rnm(command)

#print dict
