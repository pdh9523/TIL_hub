import sys; input = sys.stdin.readline

N = int(input())
M = int(input())

size = {
    "L": 3,
    "M": 2,
    "S": 1,
}

data = dict()
for i in range(1, N+1):
    s = input().strip()
    data[i] = size[s]
cnt = 0
for _ in range(M):
    s, n = input().split()
    n = int(n)
    if n not in data: continue
    if data[n] >= size[s]:
        cnt += 1
        data.pop(n)

print(cnt)
