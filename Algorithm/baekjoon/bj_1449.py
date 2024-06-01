N,L = map(int,input().split())
arr = sorted([*map(int,input().split())])

cnt = 0 
while arr : 
    start = arr.pop()
    while arr and start-arr[-1]+1 <=L : arr.pop()
    cnt += 1
print(cnt)