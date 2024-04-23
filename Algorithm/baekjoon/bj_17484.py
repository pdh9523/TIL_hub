N,M = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(N)]
DP = [[[float('inf')] * 3 for _ in range(M)] for _ in range(N)]

# 초기값 설정
for i in range(M):
    DP[0][i] = [arr[0][i]] * 3

# 리스트 순회
for i in range(1,N):
    for j in range(M):
        for dr in range(3):
            # 양끝 인덱스 제한
            if (j == 0 and dr == 2) or (j==M-1 and dr == 0):        
                continue
            # 같은 방향 제한
            for l in range(3):
                if dr != l :  
                    DP[i][j][dr] = min(DP[i][j][dr],
                                       # 방향 [j-1][j][j+1] 
                                       DP[i-1][j-dr+1][l] + arr[i][j])

# 최소값 탐색
ans = float('inf')
for i in range(M):
    ans = min(min(DP[N-1][i]), ans)
# 출력
print(ans)