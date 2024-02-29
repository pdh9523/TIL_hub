import sys
input = sys.stdin.readline

t = int(input())
tree = [list(map(int,input().split())) for _ in range(t)]

DP = [[0]*(x+1) for x in range(1,t+1)]

for i in range(t) :
    for j in range(i+1):
        DP[i][j] = max(DP[i-1][j-1], DP[i-1][j]) + tree[i][j]

print(max(DP[t-1]))