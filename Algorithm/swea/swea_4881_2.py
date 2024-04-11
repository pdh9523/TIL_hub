# 재귀함수
def backtrack(i, cnt):
    global min_sum

    if i == N:
        if min_sum > cnt:
            min_sum = cnt
    elif cnt > min_sum:
        return
    else:
        for j in range(N):
            if visited[j] == 0:
                visited[j] = 1
                backtrack(i + 1, cnt + num[i][j])   # 다음줄로 넘어감
                visited[j] = 0

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    num = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N
    min_sum = float('inf')
    backtrack(0, 0)

    print(f'#{t} {min_sum}')