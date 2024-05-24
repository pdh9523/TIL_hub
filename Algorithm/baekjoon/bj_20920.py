import sys 

input = sys.stdin.readline

N,M = map(int,input().split())
text = dict()

for _ in range(N):
    txt = input().strip()
    if len(txt) < M: continue
    text[txt] = text.get(txt,0)+1

res = list(text.items())
res.sort(key=lambda x: (-x[1],-len(x[0]),x[0]))

for i in res: 
    print(i[0])