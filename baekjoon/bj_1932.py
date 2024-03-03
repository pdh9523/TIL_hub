import sys
input = sys.stdin.readline

t = int(input())
tree = [list(map(int,input().split())) for _ in range(t)]

DP = [[0]*(x+1) for x in range(1,t+1)]

for i in range(t) :
    for j in range(i+1):
        DP[i][j] = max(DP[i-1][j-1], DP[i-1][j]) + tree[i][j]
                            # 위에서 계산된 대각선 값들에서 현재 tree값을 더해 삼각형을 만듭니다
print(max(DP[t-1]))         # 삼각형의 바닥에서 최대치를 출력