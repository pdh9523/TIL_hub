from collections import deque
from pprint import pprint

n,m,r = map(int,input().split())            # n : 지역 개수 m : 수색범위 r : 길의 개수
item = [0] + list(map(int,input().split()))

adj_lst = [[0]*(n+1) for _ in range(n+1)]

for _ in range(r):
    a,b,c = map(int,input().split())
    adj_lst[a][b]=c
    adj_lst[b][a]=c

max_value = 0
for i in range(1,n+1):
    q = deque([(i,0)])
    visit = [0] * (n+1) 
    visit[i] = 1
    ans = item[i]
    while q :
        s, dst= q.popleft()
        for idx in range(1,n+1) :
            if adj_lst[s][idx] :
                if adj_lst[s][idx] + dst <= m:
                    q.append((idx,dst+adj_lst[s][idx]))
                    visit[idx] = 1
                    ans += item[idx] 
    max_value = max(ans,max_value)
print(max_value)