#https://www.hackerrank.com/challenges/ctci-balanced-brackets/problem
# by oz

def is_matched(expression):
    if len(expression)%2 != 0:
        return False
    
    brackets={"{":"}","(":")","[":"]"}
    queue=[]
    
    for br in expression:
        if br in brackets.keys():
            queue.append(br)
        else:
            if len(queue) > 0:
                if brackets[queue.pop()]!=br:
                    return False
            else:
                return False
            
    if len(queue)==0:
        return True
    else:
        return False

t = int(raw_input().strip())
for a0 in xrange(t):
    expression = raw_input().strip()
    if is_matched(expression) == True:
        print "YES"
    else:
        print "NO"
