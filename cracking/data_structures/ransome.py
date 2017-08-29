#https://www.hackerrank.com/challenges/ctci-ransom-note
#ransom note
#by oz

def ransom_note(magazine, ransom):
    d=dict()
    for word in magazine:
        if word not in d:
            d[word]=1
        else:
            d[word]=d[word]+1
    
    for word in ransom:
        if word not in d:
            return False
        else:
            d[word]=d[word]-1
            if d[word]<0:
                return False
            
            
    return True    

m, n = map(int, raw_input().strip().split(' '))
magazine = raw_input().strip().split(' ')
ransom = raw_input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print "Yes"
else:
    print "No"
