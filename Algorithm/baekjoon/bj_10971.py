def backtrack(start, next, value, visit):

    global min_value

    # 순회 완료 시
    if all(visit):                                                     
        if arr[next][start] != 0:                                           # 마지막 마지막 동네에서 초기 지점으로 갈 수 있으면
            min_value = min(min_value, value + arr[next][start])            # 계산
        return

    if value > min_value:                                                   # 가지치기 (중간 계산 때 이미 높아진 경우)
        return
    
    for i in range(N):
        if arr[next][i] != 0 and visit[i] == 0:                             # 길 있고 방문 한적 없는 경우

            visit[i] = 1
            backtrack(start, i, value + arr[next][i], visit)                # 백트래킹
            visit[i] = 0

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

min_value = float('inf')

for i in range(N):
    visit = [0] * N
    visit[i] = 1
    backtrack(i, i, 0, visit)

print(min_value)