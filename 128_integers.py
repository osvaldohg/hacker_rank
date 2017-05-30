# Enter your code here. Read input from STDIN. Print output to STDOUT
#by oz


#input: a list of integers separated by a space
n = map(int, raw_input().strip().split(' '))

print n[0],

numBefore=n[0]

for number in xrange(1,len(n)):
    #print n[number],
    delta=n[number]-numBefore
    if abs(delta) >=128:
        print "-128",delta,
    else:
        print delta,
    
    numBefore=n[number]
    