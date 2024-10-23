from heapq import heappush, heappop


N,M = map(int,input().split())
hq = []
for _ in range(N):
    # D: 아이디어 난이도
    # P: 구현 난이도 // 구현 난이도가 높은 문제는 구현 난이도 - 구현 능력 만큼 틀렸습니다. 를 받게됨
    # T: 데이터 소유 여부 (데이터가 있는 경우 '틀렸습니다.'를 받지 않음)
    # E: 에디토리얼 소유 여부 (에디토리얼이 있고, 한별의 아이디어 능력이 아이디어 난이도의 2배 이상이면 난이도는 반씩 떨어짐)
    D,P,T,E = map(int,input().split())
    if T: P = 0
    if E: D//=2; P//=2;

    heappush(hq, (P,D))

HD,HP = map(int,input().split())
cnt = 0
ans = 0
while hq:
    p,d = heappop(hq)

    if cnt == M:
        exit(print(ans))

    if HP >= p:
        ans += 1
        HD+=1
        HP+=1
        continue
    
    if HD >= d:
        cnt += (HD-d)
        ans += 1
        HD += 1
        HP += 1
        continue


print(-1)