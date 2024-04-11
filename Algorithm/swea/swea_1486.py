def backtrack(idx = 0, total = 0):
    global ans
    if ans <= total: return
    
    if idx >= N :
        if total >= B : ans = total
        return
    backtrack(idx+1, total + staff[idx])
    backtrack(idx+1, total)

for idx in range(int(input())):
    temp = []
    N,B = map(int,input().split())
    staff = list(map(int,input().split()))
    ans = 200000
    
    backtrack()

    print(f"#{idx+1} {ans-B}")
