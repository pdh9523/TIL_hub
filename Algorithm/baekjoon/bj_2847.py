import sys
input = sys.stdin.readline

N = int(input())

arr = [int(input()) for _ in range(N)]
cnt = 0 
for i in range(N-2,-1,-1):
    while arr[i+1] <= arr[i]:
        arr[i]-=1
        cnt += 1
print(cnt)