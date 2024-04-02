import sys
input = sys.stdin.readline

N = int(input())

arr = list(map(int,input().split()))

DP = [[0]*N for _ in range(N)]

# 홀수 경우
for i in range(N):
    for j in range(N):
        if 0 <= i-j < N and 0 <= i+j < N :
            if arr[i-j] == arr[i+j] :
                DP[i-j][i+j] = 1
            else :
                break
        else :
            break
            
# 짝수 경우
for i in range(N):
    for j in range(N):
        if 0 <= i-j < N and 0 <= i+j+1 < N :
            if arr[i-j] == arr[i+1+j] :
                DP[i-j][i+j+1] = 1
            else :
                break
        else :
            break


for _ in range(int(input())):
    a,b = map(int,input().split())
    a-=1
    b-=1
    print(DP[a][b])