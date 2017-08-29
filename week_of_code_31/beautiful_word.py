#!/bin/python
#https://www.hackerrank.com/contests/w31/challenges/beautiful-word
#by oz

import sys


# Print 'Yes' if the word is beautiful or 'No' if it is not.

word=raw_input().strip()

v=["a","e","i","o","u","y"]

def check_beauty(w):
    current=w[0]
    for letter in range(1,len(w)):
        if current == w[letter]:
            return "No"
        
        elif current in v and w[letter] in v:
            return "No"
        else:
            current=w[letter]
    
    return "Yes"

if len(word)>1:
    print check_beauty(word)
else:
    print "Yes"
