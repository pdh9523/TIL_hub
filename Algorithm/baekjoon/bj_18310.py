N = int(input())
arr = sorted([*map(int, input().split())])
print(arr[(N-1)//2])
