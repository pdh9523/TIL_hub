i,j = map(int,input().split())

# i : 남북, j : 동서
# i : 12 // j : 34 
t = int(input())
# 1 : 북, 2 : 남, 3 : 서, 4 : 동
tc = [] 
for _ in range(t):
    store = list(map(int,input().split()))
    tc.append(store)

DG = list(map(int,input().split()))