import heapq

t = int(input())
q = []
for _ in range(t):
    command, *lst = map(int,input().split())
    
    if command == 0 :
        if not q:
            print(-1)
        else: 
            print(-heapq.heappop(q))
    else :
        for i in lst:
            heapq.heappush(q, -i)