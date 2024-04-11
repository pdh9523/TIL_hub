def backtrack(idx=0):
    if idx == len(empty):
        for row in arr:
            print(*row)
        exit()

    i,j = empty[idx][0], empty[idx][1]
    used = set(arr[i] + [arr[x][j] for x in range(9)] + [arr[x][y] for x in range(3*(i//3),3*(i//3)+3) for y in range(3*(j//3), 3*(j//3) +3)])
    nums = set(range(1,10))

    for num in sorted(nums-used):
        arr[i][j] = num
        backtrack(idx+1)
        arr[i][j] = 0


arr = [list(map(int,input().split())) for _ in range(9)]

empty = [(i,j) for i in range(9) for j in range(9) if not arr[i][j]]

backtrack()