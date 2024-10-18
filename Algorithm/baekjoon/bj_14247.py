N = int(input())
ans = sum([*map(int,input().split())])
arr = sorted([*map(int,input().split())])

for i in range(N):
    ans += arr[i] * i
print(ans)