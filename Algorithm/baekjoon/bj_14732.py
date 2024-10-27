import sys;input=sys.stdin.readline
arr = [[0]*501 for _ in range(501)]
for _ in range(int(input())):
    x1,y1,x2,y2 = map(int,input().split())
    for i in range(x1,x2):
        for j in range(y1,y2):
            arr[i][j] = 1
print(sum(map(sum, arr)))