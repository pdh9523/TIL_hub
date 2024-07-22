import sys
input = sys.stdin.readline
data = dict()
for _ in range(int(input())):
    x,t,c = map(int,input().split())
    data[t-x] = data.get(t-x,0)+c
print(max(data.values()))