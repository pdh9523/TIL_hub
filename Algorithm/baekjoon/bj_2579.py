t = int(input())

stair = [int(input()) for _ in range(t)]
stair.reverse()
DP = [0] * t
DP[0] = stair[0]
if t >= 2 :
    DP[1] = stair[0] + stair[1]
if t >= 3 :
    DP[2] = stair[0] + stair[2]

for i in range(3,t):
    DP[i] = max(DP[i-2]+stair[i], DP[i-3]+stair[i-1]+stair[i], DP[i])

print(max(DP))