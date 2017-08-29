#https://www.hackerrank.com/challenges/write-a-function
#by oz

def is_leap(n):
    if n%4==0:
        if n%100==0:
            if n%400==0:
                return True
            else:
                return False
            
        return True
    return False
    
year = int(raw_input())
print is_leap(year)
