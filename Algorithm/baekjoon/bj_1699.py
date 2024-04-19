N = int(input())
DP = [float('inf')] * (N+1)
sqr = []
for i in range(1,N+1):
    if i ** 2 <= N :
        sqr.append(i**2)
        DP[i**2] = 1
    else :
        break

for i in range(1,N+1):
    for num in sqr :
        if i + num < N+1 :
            DP[i+num] = min(DP[i+num],DP[i]+1)
print(DP[-1])