N = int(input())
arr = sorted([*enumerate([*map(int,input().split())])], key=lambda x: x[1])

res = [0]*N
for i in range(N) : res[arr[i][0]] = i
print(*res)