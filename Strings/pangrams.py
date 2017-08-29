# Enter your code here. Read input from STDIN. Print output to STDOUT
#!/bin/python
# https://www.hackerrank.com/challenges/pangrams/problem
# by oz

import sys
import string

alphabet=list(string.ascii_lowercase)
#print letters 

cadena=raw_input().lower().strip()
lista=cadena.split()

#print lista
status=True
for letter in alphabet:
    if letter not in cadena:
        status=False
        break
        
        
if status :
    print "pangram"
else:
    print "not pangram"
        

    
    

