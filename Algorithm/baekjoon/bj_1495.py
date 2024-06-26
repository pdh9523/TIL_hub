N,S,M = map(int,input().split())
# N 곡 개수
# S 시작 볼륨
# M 최대 볼륨
arr = [*map(int,input().split())]
DP = [set() for _ in range(N+1)]
DP[0].add(S)
for i in range(N):
    for j in DP[i]:
        if 0<=arr[i]+j<=M:
            DP[i+1].add(j+arr[i])
        if 0 <=j-arr[i]<=M:
            DP[i+1].add(j-arr[i])

print(max(DP[-1]) if DP[-1] else -1)