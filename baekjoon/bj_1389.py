from collections import deque

N,M = map(int,input().split())
adj_lst = [[] for _ in range (N+1)]
for _ in range(M) :
    a,b = map(int,input().split())
    adj_lst[a].append(b)
    adj_lst[b].append(a)
result = []
# BFS를 사용하는데, 사람들마다 다 BFS를 돌려야하나?
# print(adj_lst)
for i in range(1,N+1) :
    visit = [0] * (N+1)
    q = deque()
    q.append(i)
    while q :
        tc = q.popleft()

        for item in adj_lst[tc]:
            if visit[item] == 0:
                q.append(item)
                visit[item] = visit[tc]+1
    visit[i] = 0
    result.append([i,sum(visit)])

result.sort(key=lambda x: (x[1],x[0]))

print(result[0][0])