N,L,H = map(int,input().split())
arr = sorted([*map(int,input().split())])
print(sum(arr[L:N-H])/(N-L-H))