coins = [1,2,5,7]

N = int(input())
DP = list(range(N+1+7))

for i in range(N+1):
    for coin in coins :
        DP[i+coin] = min(DP[i+coin], DP[i]+1)
        print(DP)
print(DP[N])