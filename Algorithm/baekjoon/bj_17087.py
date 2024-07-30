from math import gcd

N,M = map(int,input().split())
arr = sorted([*map(lambda x: abs(int(x)-M), input().split())])

ans = arr[0]
for i in range(N):
    ans = gcd(arr[i],ans)
print(ans)