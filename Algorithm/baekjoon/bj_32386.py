import sys; input = sys.stdin.readline


data = dict()
for _ in range(int(input())):
    for p in input().split()[2:]:
        data[p] = data.get(p,0)+1
    
ans = 0
cnt = 0
for d in data:
    if data[d] > cnt:
        ans = d
        cnt = data[d]
    elif data[d] == cnt:
        ans = -1
print(ans)