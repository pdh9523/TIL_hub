N = int(input())

target =[[] for _ in range(10)]
seas = []
for i in range(N):
    tmp = list(map(int,input().split()))
    for n in list(range(1,7))+[9] :
        if n in tmp :
            target[n].append((i,tmp.index(n)))
