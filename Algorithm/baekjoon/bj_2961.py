# 신맛은 곱, 쓴맛은 합
def backtrack(idx=0,sour=1,bitter=0,check=False):
    global ans
    if idx == N :
        if check :
            ans = min(ans,abs(sour-bitter))
        return
    
    backtrack(idx+1,sour*tastes[idx][0],bitter+tastes[idx][1],True)
    backtrack(idx+1,sour,bitter,check)


N = int(input())

tastes = [ [*map(int,input().split())] for _ in range(N) ]

ans = float('inf')
backtrack()
print(ans)