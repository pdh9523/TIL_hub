k,a,b=map(int,input().split())
ans = 0
if a*b>=0: # 범위의 수직선 방향이 같은 경우
    ans = b//k-a//k
    if a%k==0: ans += 1
else : # 범위의 수직선 방향이 다른 경우 
    ans = abs(b)//k + abs(a)//k + 1
print(ans)