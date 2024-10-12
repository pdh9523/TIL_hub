import sys; input = sys.stdin.readline


N = int(input())
arr = [int(input()) for _ in range(N)]
if N == 1: exit(print(1))

if arr[0] >= arr[1]: print(1)

for i in range(1,N-1):
    if arr[i-1] <= arr[i] >= arr[i+1] : print(i+1)

if arr[-2] <= arr[-1]: print(N)