import sys
input = sys.stdin.readline

for _ in range(int(input())):
    arr = [list(map(int,input().split())) for _ in range(int(input()))]

    arr.sort()
    
    DP = [[1] * len(arr) for _ in range(len(arr))]

    for i in range(len(arr)):
        tmp = i
        for j in range(i, len(arr)):
            if arr[tmp][1] > arr[j][1]:
                DP[i][j] = DP[i][tmp] +1
                tmp = j
            else :
                DP[i][j] = DP[i][j-1]
    print(max([max(x) for x in DP]))