import sys

input = sys.stdin.readline

for _ in range(int(input())):
    t = int(input())
    arr = list(map(int,input().split()))
    tmp, ans = 0,0
    for i in range(t-1,-1,-1):
        if arr[i] > tmp:
            tmp = arr[i]
        else :
            ans += tmp-arr[i]
    print(ans)