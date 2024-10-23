import sys; input = sys.stdin.readline


arr = []
for _ in range(int(input())):
    start,end = map(int,input().split())
    arr.append((start,1))
    arr.append((end, -1))

arr.sort()
ans,cur = 0,0
for time, event in arr:
    cur += event
    ans = max(ans, cur)
print(ans)