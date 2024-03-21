N,M = map(int,input().split())

S = list(input())
T = list(input())
sdx = []
tdx = []
for i in range(len(S)):
    if S[i] == "1":
        sdx.append(i)

for j in range(len(T)):
    if T[j] == "1":
        tdx.append(j)
tmp = 0
for idx in range(M):
    tmp += abs(sdx[idx] - tdx[idx])
ans = (tmp//2)**2 + (tmp-tmp//2)**2

print(ans)