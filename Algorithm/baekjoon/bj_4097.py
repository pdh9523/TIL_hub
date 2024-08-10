import sys
input = sys.stdin.readline

while True:
    N = int(input())
    if N == 0 : break

    arr = [int(input()) for _ in range(N)]

    DP = [0]*N
    
    DP[0] = arr[0]

    for i in range(1,N):
        DP[i] = max(DP[i-1] + arr[i], arr[i])
    
    print(max(DP))