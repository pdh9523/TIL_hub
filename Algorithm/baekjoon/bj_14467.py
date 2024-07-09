data = dict()
cnt = 0
for _ in range(int(input())):
    a,b = map(int,input().split())
    if a in data:
        if data[a] != b: cnt += 1
    data[a]=b
print(cnt)