from heapq import heappop, heappush

N,M = map(int,input().split())
hq = [(0,M)]

if N-M>0: 
    print(N-M)
    print(1)
    exit()

step = 0
cnt = 0
visit = [0]*100002

while hq:
    dist_now, now = heappop(hq)
    visit[now]=1

    if now > 100000 or now < 0: continue

    if (not step or step == dist_now) and now == N:
        step = dist_now
        cnt += 1
        continue

    if step and dist_now>step: continue

    if not now%2 and not visit[now//2]:
        heappush(hq,(dist_now+1, now//2))
    if not visit[now-1]:
        heappush(hq,(dist_now+1, now-1))
    if not visit[now+1]:
        heappush(hq,(dist_now+1, now+1))

print(step)
print(cnt)