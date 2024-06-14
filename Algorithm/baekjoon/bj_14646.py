N = int(input())
arr = [*map(int,input().split())]

res = [0]*(N+1)
tmp,ans = 0,0

for i in arr :
    if res[i] == 0:
        res[i] = 1
        tmp += 1
    else :
        res[i] = 0
        tmp -= 1
    ans = max(tmp,ans)
    
print(ans)