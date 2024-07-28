N,M = map(int,input().split())

t=N//2+2
for i in range(3,t+1):
    if i*(t-i) == N+M:
        exit(print(t-i,i))