tc = 0
while True :
    tc += 1
    N = int(input())

    if N == 0 :
        break

    graph = dict()
    for _ in range(N):
        a,b = input().split()
        graph[a] = b 
    cnt = 0
    visit = dict()
    for i in graph :
        if not visit.get(i):
            stack = [i]
            check = False
            while stack:
                now = stack.pop()
                if not visit.get(now):
                    visit[now] = 1
                    stack.append(graph[now])
                    check = True
            if check :
                cnt += 1
    print(tc, cnt)