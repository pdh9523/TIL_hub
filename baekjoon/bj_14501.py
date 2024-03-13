N = int(input())

DP = [0]*(N+6)

for day in range(1,N+1):
    T,P = map(int,input().split())

    DP[day+T-1] = max(P, DP[day-1]+P,DP[day+T-1])
    DP[day] = max(DP[day-1], DP[day])

print(DP[N])