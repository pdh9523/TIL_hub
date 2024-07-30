import sys
input = sys.stdin.readline

ans = 0
tmp = 0
for _ in range(int(input())):
    a,b = map(int,input().split())

    tmp += b
    if tmp > 0:
        ans = max(ans,tmp)
    tmp -= a
print(ans)