'''
공유기 설치 골4 이분탐색
이분탐색 싫어
가능한 공유기 사이의 거리를 이분탐색을 통해 찾아나간다.
'''
import sys; input = sys.stdin.readline


def is_available():
    cur = arr[0]
    cnt = 1
    for i in range(1,N):
        if arr[i] >= cur+mid:
            cnt += 1
            cur = arr[i]
    
    return cnt >= M
    

N,M = map(int,input().split())
arr = sorted([int(input()) for _ in range(N)])

start = 1
end = arr[-1] - arr[0]


ans = 0
while start <= end:
    mid = (start+end) // 2
    if is_available():
        start = mid+1
        ans = mid
    else:
        end = mid-1

print(ans)