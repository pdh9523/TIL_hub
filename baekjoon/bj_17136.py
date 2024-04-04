# 10*10 종이가 주어지고, 모든 1을 덮는 데 필요한 색종이의 최소 개수를 출력
# 색종이는 1*1 부터 5*5까지 각 5개 있음
def backtrack(i=0,j=0,cnt=0):                           # 백트래킹 시행
    global ans

    if i > 9 :                                          # 가로 순회 완료시
        backtrack(0, j+1, cnt)                          # 다음 세로열 순회
        return
    
    if j > 9 :                                          # 세로도 다 순회시
        ans = min(ans, cnt)                             # 결과 비교
        return
    

    # 백트래킹
    if paper[i][j] :                                    # 종이가 1이면
        for size in range(4,-1,-1):                     # 색종이 큰거부터 비교
            if colors[size] == 0 :                      # 쓰려는 색종이를 다 썼으면
                continue                                # 넘어감
            if i + size > 9 or j + size > 9 :           # 붙였는데 더 크면
                continue                                # 넘어감
                
            check = False  
            for x in range(i, i+size+1):                # 네모 공간이 다 1인지 확인
                for y in range(j, j+size+1):        
                    if not paper[x][y]:                 # 쓰려는 색종이 크기에 0이 있으면
                        check = True
                if check :                              # 탈출
                    break

            else :                                      # 색종이를 붙일 수 있으면 (백트래킹 시작)
                for x in range(i, i+size+1):
                    for y in range(j, j+size+1):
                        paper[x][y] = 0                 # 그 위치를 다 0으로 만들고 
                
                colors[size] -= 1                       # 색종이 한장 빼고
                backtrack(i+size+1, j, cnt+1)           # 백트래킹 넘어가고
                colors[size] += 1                       # 원위치
            
                for x in range(i, i+size+1):            # 원위치 
                    for y in range(j, j+size+1):
                        paper[x][y] = 1

    else :                                              # 종이가 0이면 그냥 한칸 넘어가서 백트래킹
        backtrack(i+1, j, cnt)

paper = [list(map(int,input().split())) for _ in range(10)]
colors = [5,5,5,5,5]          # 인덱스마다 하나씩 놔두기

ans = float('inf')

backtrack()

print(ans if ans != float('inf') else -1)