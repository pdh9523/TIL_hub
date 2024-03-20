import sys
input = sys.stdin.readline

t = int(input())

wine = [0] + [int(input()) for _ in range(t)]

DP = [0]*(t+1)

DP[1] = wine[1]
if t > 1:
    DP[2] = wine[1]+wine[2]

for i in range(3,t+1):
    DP[i] = max(max(DP[:i-1])+wine[i], max(DP[:i-2])+wine[i-1]+wine[i])
print(max(DP))