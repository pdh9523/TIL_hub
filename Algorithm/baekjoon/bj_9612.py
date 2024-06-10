import sys

input = sys.stdin.readline


N = int(input())
tmp = 0
ans = ""
txt = dict()
for _ in range(N):
    a = input().strip()
    txt[a] = txt.get(a,0)+1

    for k,v in txt.items():
        if v >tmp:
            tmp = v 
            ans = k
        if v==tmp:
            ans = max(ans,k)
print(ans,tmp)