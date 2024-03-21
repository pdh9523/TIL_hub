# 맥주 마시면서 걸어가기 최고
import sys
from collections import deque

input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())

    home = tuple(map(int,input().split()))

    conv = [list(map(int,input().split())) for _ in range(N)]

    concert = list(map(int,input().split()))
    conv.append(concert)

    dq = deque([home])
    visit = [0] * (N+1)
    while dq :
        i, j = dq.popleft()

        if concert == [i,j] :
            print("happy")
            break
        
        for idx in range(len(conv)) :
            if not visit[idx] :
                p,q = conv[idx][0], conv[idx][1]

                if abs(p-i)+abs(q-j) <= 1000:
                    visit[idx] = 1
                    dq.append((p,q))
    else :
        print("sad")