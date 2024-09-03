def backtrack(idx=0, res=""):
    global cnt
    if idx == N:
        if arr.issubset(set(res)):
            cnt += 1
        return
    
    for i in range(10):
        backtrack(idx+1, res+str(i))


N,M = map(int,input().split())
arr = set()
if M: arr = set(input().split())
cnt = 0 
backtrack()
print(cnt)