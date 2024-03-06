def f(num, i, idx):
    global max_num

    if i == N:
        if max_num < num:
            max_num = num

    else:
        if len(sums[i - 1][idx]) >= 2:
            if num != max(sums[i - 1][idx]):
                return

        sums[i-1][idx].append(num)
        for k in range(2):
            f(num + triangle[i][idx + k], i + 1, idx + k)

N = int(input())
triangle = [list(map(int, input().split())) for _ in range(N)]

max_num = 0
sums = []
for i in range(N - 1):
    sums.append([[] for _ in range(i + 1)])
f(triangle[0][0], 1, 0)

print(max_num)