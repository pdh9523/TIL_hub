def convert(n): return ans[n]

N = sum(map(int,input().split()))
arr = [[*map(int,input().split())] for _ in range(int(input()))]
brr = []
ans = [2]*(N+1)
for i,j,k,r in arr:
    if r == 1: ans[i]=ans[j]=ans[k]=1
    else : brr.append((i,j,k))

## 고장 정상 정상인 경우 고장 확정
for i,j,k in brr:
    # 오답 이유 : ans[i]+ans[j]+ans[k] ==4로 검증했었는데,
    # 2,2,0 인 경우 예외처리가 되지 않아 0,0,0으로 처리됨
    if (ans[i],ans[j],ans[k]).count(1) == 2:
        for d in i,j,k:
            if ans[d]==2 : ans[d]=0

print(*ans[1:], sep="\n")