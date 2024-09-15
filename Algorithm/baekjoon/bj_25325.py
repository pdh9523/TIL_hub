import sys; input=sys.stdin.readline


N = int(input())
data = dict()
for _ in range(N+1):
    arr = input().split()
    for char in arr:
        data[char] = data.get(char, -1) + 1

res = sorted(data.keys(), key=lambda x: -data[x])

for i in res:
    print(i, data[i])