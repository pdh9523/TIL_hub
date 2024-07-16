import sys
input = sys.stdin.readline

def backtrack(i, result):
    if len(result) == 5:
        exit(print(1))
    for j in tree[i]:
        if j not in result:
            backtrack(j, result|{j})

N,M = map(int,input().split())

tree = [[] for _ in range(N)]
for _ in range(M):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

for i in range(N):
    backtrack(i,{i,})
print(0)