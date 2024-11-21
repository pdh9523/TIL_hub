def lis(n):
    start,end = 0, len(ans)-1

    while start <= end:
        mid = (start+end) // 2
        
        if ans[mid] == n:
            return mid
        
        if ans[mid] < n: 
            start = mid + 1
        else: 
            end = mid - 1
    return start


N = int(input())
arr = [*map(int,input().split())]

ans = [arr[0]]

for item in arr:
    if ans[-1] < item:
        ans.append(item)
    else:
        nxt = lis(item)
        ans[nxt] = item

print(len(ans))