fibo = [0,1,1,2]

t = int(input())


i = 4
while len(fibo) != t+1:
    a = fibo[i-2]%1000000007
    b = fibo[i-1]%1000000007
    
    if a+b in fibo : 
        i = fibo.index(a+b)
    else :
        i += 1
    fibo.append(a+b)

print(fibo[t]%1000000007)