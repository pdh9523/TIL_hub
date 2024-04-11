t = int(input())

DP = [1,1]

for i in range(1,t):
    DP.append((DP[i]+DP[i-1])%15746)

print(DP[t])