# @param A : tuple of integers
# @return an integer

def repeatedNumber(self, A):
    buff={}
    for number in A:
        if number in buff:
            return number
        else:
            buff[number]=1
        
    return -1