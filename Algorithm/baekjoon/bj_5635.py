N = int(input())
info = dict()
for _ in range(N):
    name, d,m,y = input().split()
    age = int(y)*365*12*30 + int(m)*30 + int(d)
    info[name] = age

minv=float('inf')
minn=""
maxv=0
maxn=""
for key,value in info.items():
    if minv > value:
        minv=value
        minn=key
    if value > maxv :
        maxv=value
        maxn=key
print(minn)
print(maxn)