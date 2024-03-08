M,N,H = map(int,input().split())

tomatoes = [[[]for _ in range(M)] for _ in range(N)]
for h in range(H):
    for i in range(N):
        tomato = list(map(int,input().split()))
        for j in range(M):
            tomatoes[i][j].append(tomato[j])

# 토마토 이동 방향 : 위 아래(리스트 내부 인덱스 +/- 1), 델타(리스트의 같은 인덱스 내 델타탐색)
            
