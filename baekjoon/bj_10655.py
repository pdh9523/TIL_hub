import sys

input = sys.stdin.readline

N = int(input())

check = [tuple(map(int,input().split())) for _ in range(N)]
ans = 0
tmp = 0
max_value = 0
for i in range(N-1):
    # 멘하탄 거리 기본 공식
    dist = abs(check[i+1][0] -check[i][0]) + abs(check[i+1][1] - check[i][1])

    ans += dist
    # 두 체크 포인트를 각각 지나갔을 때와, 건너 뛰었을 때의 값의 차이를 비교
    if i < N-2 :    # i+2 조건으로 인해 인덱스 제한
        tmp = abs(check[i+2][0] - check[i+1][0]) + abs(check[i+2][1] - check[i+1][1]) + dist - (abs(check[i+2][0] - check[i][0]) + abs(check[i+2][1] - check[i][1]))

    # 그 중 차이가 가장 심한 값을 저장
    max_value = max(max_value,tmp)

print(ans-max_value)