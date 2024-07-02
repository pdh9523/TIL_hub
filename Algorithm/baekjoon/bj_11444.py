def fibonacci(n):
    if n in fibo: return fibo[n]

    half = n//2

    if n%2:
        left = fibonacci(half)
        right = fibonacci(half+1)
        fibo[n] = (left**2 + right**2)%dv
        return fibo[n]
    else :
        left = fibonacci(half-1)
        right = fibonacci(half)
        fibo[n] = ((2*left+right)*right)%dv
        return fibo[n]
    

N = int(input())
fibo = dict()
dv = 1000000007
fibo[1], fibo[2] = 1, 1
print(fibonacci(N))
