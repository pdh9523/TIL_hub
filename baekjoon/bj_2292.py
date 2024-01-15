# 1 + 6 + 12 + 18 + 24 + ---
a = int(input())

n =(a-1)//6

def gause(n) :
    a=0
    while True : 
        if (1+a)*a/2 > n :
            return a
        else : 
            a+=1

print(gause(n)+1)