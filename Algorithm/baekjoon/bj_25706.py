N = int(input())
a = [*map(lambda x:int(x)+1,input().split())]
D = [1]*N
for i in range(N-1,-1,-1):
    if i+a[i]<N:D[i]=D[i+a[i]]+1
print(*D)