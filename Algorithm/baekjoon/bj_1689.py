import sys
input = sys.stdin.readline

data = dict()
for _ in range(int(input())):
    s,e = map(int,input().split())
    data[s] = data.get(s,0)+1
    data[e] = data.get(e,0)-1

tmp,ans = 0,0
for key in sorted(data):
    tmp += data[key]
    ans = max(ans,tmp)
print(ans)