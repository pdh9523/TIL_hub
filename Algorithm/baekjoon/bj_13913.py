#2390 9139

from collections import deque


N,M = map(int,input().split())

if N > M : 
    print(N-M)
    print(*list(range(N,M-1,-1)))
    exit()

else :
    vst = [False] * 100001
    q = deque([(N,[N])])
    vst[N] = 1
    while q :
        now, visit = q.popleft()

        if now == M :
            print(len(visit)-1)
            print(*visit)
            exit()

        if now < M :
            if now*2 <= 100000 and not vst[now*2] :
                vst[now*2] = True
                q.append((now*2, visit+[now*2]))
            if now <= 100000 and  not vst[now+1] :
                vst[now+1] = True
                q.append((now+1, visit+[now+1]))
        if now > 0 and not vst[now-1] :
            vst[now-1] = True
            q.append((now-1, visit+[now-1]))



# from collections import deque

# n, k = map(int, input().split())
# v = [-1 for _ in range(100001)]
# move = [-1 for _ in range(100001)]

# def bfs(start):
# 	q = deque()
# 	q.append(start)
# 	v[start] = 0
# 	while q:
# 		idx = q.popleft()
# 		if idx == k:
# 			return 
# 		for i in [idx-1, idx+1, idx*2]:
# 			if 0 <= i <= 100000 and v[i] == -1:
# 				v[i] = v[idx]+1
# 				q.append(i)
# 				move[i] = idx
# bfs(n)
# print(v[k])

# ans = []
# for i in range(v[k]+1):
# 	ans.append(k)
# 	k = move[k]
# print(*ans[::-1])