N = int(input())
mod = 1000000

# 연속 3일 결석 하면 안되니까, 연속 0일,1일,2일 결석을 저장
DP = [[0]*3 for _ in range(N+1)]
DP[0] = [1,0,0]
DP[1] = [1,1,0]

for i in range(2,N+1):
    # 출석하면 
    DP[i][0] = (DP[i-1][0] + DP[i-1][1] + DP[i-1][2])%mod
    # 출석 안하면
    DP[i][1] = DP[i-1][0]
    #
    DP[i][2] = DP[i-1][1]

data = [*map(sum, DP)]

tmp = 0
for i in range(N):
    tmp += (data[i]*data[N-1-i])%mod
print((data[N]+tmp)%mod)