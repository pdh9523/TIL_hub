import sys
from collections import deque

input = sys.stdin.readline

N,M = map(int,input().split())

tree = [[] for _ in range(N+1)]

for _ in range(M):
    A,B = map(int,input().split())
    tree[B].append(A)

result= [0]

for i in range(1,N+1):
    q = deque([i])
    visit = [0] * (N+1)
    count = 0
    while q :
        a = q.popleft()
        visit[a] = 1
        count += 1
        for item in tree[a] :
            if visit[item] == 0 :
                q.append(item)
    result.append(count)
k = max(result)
ans = enumerate(result)
for key,value in ans :
    if value == k :
        print(key, end=" ")