for _ in range(int(input())):
    x1,y1,r1, x2,y2,r2 = map(int,input().split())

    dist = ((x1-x2)**2 + (y1-y2)**2)**0.5
    data = (r1, r2, dist)
    maxv = max(data)
    rest = sum(data)-maxv

    if dist==0 and r1==r2 : print(-1)
    elif maxv > rest : print(0)
    elif dist==r1+r2 or maxv == rest : print(1)
    else : print(2)