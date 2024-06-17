N,M=map(int,input().split())
trees=[*map(int,input().split())]
start,end = 1,max(trees)

while start <= end:
    mid = (start+end)//2

    res = 0
    for tree in trees:
        if tree >= mid:
            res += tree-mid

    if res >=M:
        start = mid+1
    else :
        end = mid-1
print(end)