N = int(input())

arr = dict(zip([*map(int,input().split())],[1]*N))
M = int(input())
target = [*map(int,input().split())]
for i in target:
    print(arr.get(i,0), end=" ")