from heapq import heappush, heappop


N,M = map(int,input().split())
hq = []
for _ in range(N):
    # D: 아이디어 난이도
    # P: 구현 난이도
    # T: 데이터 소유 여부
    # E: 에디토리얼 소유 여부
    D,P,T,E = map(int,input().split())
    heappush(hq,(D,P,T,E))

