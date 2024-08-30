from collections import Counter

N = int(input())
arr = Counter([*map(int,input().split())])

ans = 0

for k in arr:
    if k==arr[k]:
        ans = max(ans,k)
if ans == 0 and 0 in arr:
    exit(print(-1))
print(ans)