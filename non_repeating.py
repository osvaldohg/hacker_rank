#!/bin/python
#non-repeating
#Find the first non repeating character in a string.
#For example if the input string "abcdeabc", non repeating character is "e"

def find_repeating(word):
    letters=[0 for x in range(97,123)]
    
    for i in range(0,len(word)):
        pos=ord(word[i])-97
        if letters[pos]==0:
            letters[pos]+=1
        else:
            return word[i-1]
    
    return "no duplicate"

print find_repeating("abcdeabc")
print find_repeating("abcdefg")
print find_repeating("a")

