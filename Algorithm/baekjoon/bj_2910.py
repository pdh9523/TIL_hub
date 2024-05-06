N,C = map(int,input().split())
arr = [*map(int,input().split())]

result = dict()
for num in arr :
    result[num]=result.get(num,0)+1
ans = sorted(result.items(), key=lambda x : x[1], reverse=True)

for k,v in ans :
    for _ in range(v):
        print(k, end=" ")