def backtrack(idx=0, res=0):
    data.add(res)
    if idx == N:
        return
    
    backtrack(idx+1, res+arr[idx])
    backtrack(idx+1, res)
    
    
N = int(input())
arr = [*map(int,input().split())]
M = sum(arr)

data = set() # 여기가 원인인듯

backtrack()
print(M+1-len(data))