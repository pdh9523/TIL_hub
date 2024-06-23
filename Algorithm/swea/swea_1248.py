for tc in range(int(input())):
    V,E,N,M=map(int,input().split())
    data = [*map(int,input().split())]

    tree = [[] for _ in range(V+1)]
    for i in range(0,E*2,2):
        tree[data[i]].append(data[i+1])
    
    