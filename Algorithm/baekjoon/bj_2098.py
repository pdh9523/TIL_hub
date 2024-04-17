import sys

input = sys.stdin.readline


N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

dp = {}

def DFS(now=0, visit=1) :
    # 방문을 마친 경우
    if visit == (1 << N) - 1 :
        # 돌아갈 길이 있으면
        if arr[now][0]:
            # 돌아가는 길의 값을 반환
            return arr[now][0]
        # 돌아가는 길이 없으면
        else :
            # 돌아가지 못함 (큰 수 반환)
            return int(1e9)
    
    # DP에 이미 저장된 길이라면
    if (now,visit) in dp:
        # DP의 값을 반환
        return dp[(now, visit)]
    

    # 최소치 갱신
    min_cost = int(1e9)

    # 1부터 N까지 순회하면서
    for next in range(1,N):
        # 길이 없거나, 이미 방문했다면 다음 순회로 넘어가고
        if arr[now][next] == 0 or visit & ( 1 << next) :
            continue
        # 다음 위치로 이동하여 재귀 호출하고, 방문 표시
        cost = DFS(next, (visit | (1<<next))) + arr[now][next]

        # 최소 비용 갱신
        min_cost = min(min_cost, cost)
    # DP 에 최소 비용 저장
    dp[(now,visit)] = min_cost

    # 최소 비용 반환
    return min_cost

print(DFS())