for tc in range(int(input())):
    # 물건 개수 N 
    # 가방 크기 K
    N,K = map(int,input().split())
    
    DP = [ [0] * (K+1) for _ in range(N+1) ]
    things =[[0,0]] + [ [*map(int,input().split())] for _ in range(N)]

    for i in range(N+1):
        for j in range(K+1):

            if j < things[i][0]:
                DP[i][j] = DP[i-1][j]
            else:
                DP[i][j] = max(DP[i-1][j-things[i][0]]+things[i][1], DP[i-1][j])
    print(f"#{tc+1} {DP[N][K]}")