from collections import deque

N = int(input())
arr = deque(sorted([*map(int,input().split())]))
ans = 0
while len(arr)>1:
    arr.popleft()
    ans += 2*arr.pop()
if arr:
    ans += arr.pop()
print(ans)