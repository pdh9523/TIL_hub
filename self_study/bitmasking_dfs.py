import sys
input = sys.stdin.readline

N = int(input())
arr = [ [*map(int,input().split())] for _ in range(N) ]
# 0 : 초기 좌표 / 1 : 초기 visit / 2 : 합
stack = [(0,1,0)]
DP = {}
ans = float('inf')
while stack :
    now , visit, dist = stack.pop()

    # 모든 도시를 방문한 경우
    if visit == ( 1 << N ) - 1 :
        if arr[now][0] :
            ans = min(ans, dist+arr[now][0])
            continue 

    if (now,visit) in DP :
        DP[(now,visit)] = min(DP(now,visit),dist)
        continue

    for next in range(1,N):
        if arr[now][next] != 0 and not visit & ( 1 << next ) :
            stack.append((next,visit|1<<next, dist+arr[now][next]))

print(ans)



#### 재귀
def dfs(now=0, visit=1):
    # 모두 방문 완료한 경우
    if visit == (1<<N) - 1 :
        # 돌아갈 길이 있으면
        if arr[now][0]:
            # 그 길을 반환
            return arr[now][0]
        # 돌아갈 수 없으면,
        else :
            # 밑에서 최소치 비교를 막아 길을 없앰
            return float('inf')
    
    # DP 에 이미 길을 지나간게 있으면 (계속 최소치로 갱신)
    if (now,visit) in DP :
        # DP에 저장된 값을 반환
        return DP[(now,visit)]

    # 최소치 초기화
    min_value = float('inf')
    # 1 부터 N-1 까지 순회하면서
    for next in range(1,N):
        # 값이 있고, 방문 하지 않았을 경우
        if arr[now][next] and not (visit & (1 << next)) :
            # 방문하여 재귀 호출한 값을 cost에 더하고
            cost = dfs(next, (visit|1<<next)) + arr[now][next]
            # 재귀에서 벗어난 결과를 min_value와 비교한다
            min_value = min(min_value, cost)
            
    # DP에 방문값을 저장
    DP[(now,visit)] = min_value

    return min_value

N = int(input())
arr = [ [*map(int,input().split())] for _ in range(N)]
DP = dict()
print(dfs())