def backtrack(idx=0, res=0):
    if idx==N:
        return
    
    backtrack(idx+1, res+arr[idx])
    backtrack(idx+1, res)
    backtrack(idx+1, abs(res-arr[idx]))

    data.add(res+arr[idx])
    data.add(res)
    data.add(abs(res-arr[idx]))

N = int(input())
arr = [*map(int,input().split())]
max_value = max(arr)
data = set()
backtrack()

print(sum(arr)-len(data)+1) # 0이 data에 포함