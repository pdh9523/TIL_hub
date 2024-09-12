*stat,N = map(int,input().split())
ans = N*4-sum(stat)
print(ans if ans>0 else 0)