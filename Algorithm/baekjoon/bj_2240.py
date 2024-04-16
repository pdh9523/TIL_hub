import sys
input = sys.stdin.readline

T,W = map(int,input().split())

DP = [[0] * (W+1) for _ in range(T)]

for t in range(T):
    fruit = int(input())
    for w in range(W+1):
        if fruit == 1 and w % 2 == 0 :
            DP[t][w] = max(DP[t-1][0:w+1]) + 1
        elif fruit == 2 and w % 2 == 1 :
            DP[t][w] = max(DP[t-1][0:w+1]) + 1
        else :
            DP[t][w] = max(DP[t-1][0:w+1])


print(max(DP[-1]))