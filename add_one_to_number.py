#by oz

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, a):
        
        while a[0]==0 and len(a)>1:
            a.pop(0)
        
        plus=0
        a[len(a)-1]=a[len(a)-1]+1
        if a[len(a)-1]>=10:
            a[len(a)-1]=a[len(a)-1]%10
            plus=1
        else:
            plus=0
                
        for i in range(len(a)-2,-1,-1):
            a[i]=a[i]+plus
            if a[i]>=10:
                a[i]=a[i]%10
                plus=1
            else:
                plus=0
        
        if plus!=0:
            a.insert(0,plus)
        return a