def fibo(n) :
    rem = {0:0, 1:1, 2:1}

    for i in range(3,n+1) :
        rem[i] = rem[i-1] + rem[i-2]
    
    return rem[n]
a=int(input())
print(fibo(a))