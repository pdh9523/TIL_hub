# 합이 15
check = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]

def backtrack(idx=0,visit=[]):
    global ans
    for a,b,c in check:
        if c < len(visit) and visit[a]+visit[b]+visit[c]!=15:
            return

    if idx == 9:
        for a,b,c in check:
            if visit[a]+visit[b]+visit[c]!=15:
                break
        else :
            tmp = 0
            for i in range(9):
                tmp += abs(visit[i]-arr[i])
            ans = min(ans,tmp)
        return 

    for i in range(1,10):
        if i not in visit:
            backtrack(idx+1,visit+[i])
    
arr = []
for _ in range(3):
    arr += [*map(int,input().split())]
ans = float('inf')
backtrack()
print(ans)