import sys; input = sys.stdin.readline


def bi_search(n):
    now = arr[0] + n
    cnt = 1
    for i in arr[1:]:
        if now >= i: continue
        cnt += 1
        now = i+n
    if K >= cnt: return True


N,K = map(int,input().split())
arr = [*map(int,input().split())]

if K >= N: exit(print(1))
if K == 1:
    if N == 1:
        exit(print(1))
    else:
        exit(print(arr[-1]-arr[0]+1))
start = 1
end = arr[-1] - arr[0]
# 이분 탐색
while start < end:
    now = (start+end)//2
    if bi_search(now):
        end = now
    else:
        start = now + 1
    
print(now+1)