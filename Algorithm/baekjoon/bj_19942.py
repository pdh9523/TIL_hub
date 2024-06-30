def backtrack(i, cnt, result, visit=[], cost=0):
    global ans, vst 
    
    for a,b in zip(nutrient, result):
        if a > b : break
    else :
        if ans > cost:
            ans = cost
            vst = visit
        return

    if i == N: return

    backtrack(i+1, cnt+1, list(map(sum, zip(result,foods[i]))), visit+[i+1], cost+foods[i][-1])
    backtrack(i+1, cnt, result, visit, cost)

N = int(input())
nutrient = [*map(int,input().split())]
foods = [[*map(int,input().split())] for _ in range(N)]

ans = float('inf')
vst = ""
backtrack(0,0,[0]*len(nutrient))
print(ans if ans != float('inf') else -1)
if vst:print(*vst)