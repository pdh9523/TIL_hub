arr = range(1, int(input()) + 1)
brr = [*map(int, input().split())]

ans = 0
for i, j in zip(arr, brr):
    if i != j:
        ans += 1
print(ans)
