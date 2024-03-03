t = int(input())

stair = [0] + [int(input()) for _ in range(t)]

DP = [0] * (2*t)
DP[1] = stair[1]
DP[2] = stair[2]
DP[3] = stair[1]+stair[3]

for idx in range(4,t+1):
    DP[idx] = max((DP[idx-3] + stair[idx-2] + stair[idx]),(DP[idx-2] + stair[idx]))

DP[idx] = max(DP[idx-1]+stair[idx], DP[idx-2]+stair[idx])
print(DP[t])