import sys

input = sys.stdin.readline

N = int(input())

tmp = dict()
for _ in range(N):
    num = int(input())
    tmp[num] = tmp.get(num,0)+1

ans = 0
res = 0

for i in sorted(tmp.keys()) :
    if tmp[i] > res :
        ans = i
        res = tmp[i]

print(ans)