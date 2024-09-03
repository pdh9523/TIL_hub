def bi_search(mid):
    if arr[1]-arr[0] > mid:
        return False
    
    if arr[-1] - arr[-2] > mid:
        return False

    for i in range(1, M):
        if (arr[i+1] - arr[i]) / 2 > mid:
            return False
    return True


N,M = int(input()), int(input())
arr = [0]+[*map(int,input().split())]+[N]

start,end,ans = 0,N,0
while start<=end:
    mid = (start+end) // 2
    if bi_search(mid):
        end = mid - 1
        ans = mid
    else: start = mid + 1
print(ans)