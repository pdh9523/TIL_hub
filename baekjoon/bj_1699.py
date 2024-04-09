from math import sqrt

N = int(input())
n = int(sqrt(N)) 
DP = [0] * (n+1)

for i in range(1,n+1):
    a = N
    cnt = 0
    while a > 0 :
        target = i
        while target**2 > a :
            target -= 1
        a -= target**2
        cnt += 1
    DP[i] = cnt

print(min(DP[1:]))