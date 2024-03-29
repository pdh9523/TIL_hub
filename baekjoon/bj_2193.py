N = int(input())

DP = [[0,0] for _ in range(N)]

# DP[N][0] : 끝자리가 0으로 끝나는 경우 /// DP[N][1] : 끝자리가 1로 끝나는 경우

DP[0][1]=1

for i in range(1,N):
    DP[i][0] = DP[i-1][0] + DP[i-1][1]  # 0으로 끝나는 경우, 이전 길이에서 끝이 0인 경우와 1인 경우 에서 0을 붙이면 됨
    DP[i][1] = DP[i-1][0]               # 1로 끝나는 경우, 이전 길이에서 끝이 0이었던 것에서 1을 붙이면 됨 

print(sum(DP[N-1]))                     # 0으로 끝나는 경우와 1로 끝나는 경우 합해서 출력