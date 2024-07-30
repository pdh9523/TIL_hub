N = int(input())
arr = [*map(int,input().split())]
ans = 0

for s in range(1, 9):
    left = 0
    while left < N:
        right = left
        while right < N and s <= arr[right] <= s+2:
            right += 1
        ans = max(ans, right - left)
        left = right + 1

print(ans)
