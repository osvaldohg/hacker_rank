# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/flipping-bits/problem
# by oz

def complete32(number):
    fbinary=bin(number)
    binary=fbinary[2:]
    size=len(binary)
    comp="00000000000000000000000000000000"
    dif=32-size
    fullbinary=comp[:dif]+binary
        
    return fullbinary
  
def flip(number):
    word=list(number)
    #print word
    for i in range(0,len(number)):
        if word[i]=="0":
            word[i]="1"
        else:
            word[i]="0"
    return word

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    a=complete32(n)
    #print a
    #print flip(a)
    flipped=flip(a)
    chain=""
    for letter in flipped:
        chain+=letter
        
    #print chain
    print int(chain,2)
    
    