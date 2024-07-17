import sys

sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline


def union(v1, v2):
    r1 = find(v1)
    r2 = find(v2)

    if rank[r1] > rank[r2]:
        root[r2] = r1
    elif rank[r1] < rank[r2]:
        root[r1] = r2
    else:
        root[r2] = r1
        rank[r1] += 1


def find(v):
    if v == root[v]:
        return v
    root[v] = find(root[v])
    return root[v]


n, m = map(int, input().split())
root = [i for i in range(n)]
rank = [0]*n
conn = [0]*m

for i in range(m):
    a, b = map(int, input().split())
    if find(a) == find(b):
        exit(print(i + 1))
    union(a, b)
print(0)

