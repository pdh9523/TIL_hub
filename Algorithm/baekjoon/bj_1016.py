from math import ceil


N,M = map(int,input().split())

ans = M-N +1
arr = [False] * M+1

for i in range(2, int(M**0.5)+1):
    sqr = i**2
    for j in range((ceil(N/sqr))*sqr, M+1, sqr):
        if not arr[j]:
            arr[j] = True
            ans -= 1
print(ans)
