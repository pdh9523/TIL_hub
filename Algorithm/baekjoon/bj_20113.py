from collections import Counter


N = int(input())
arr = Counter(map(int,input().split()))

max_value = 0
ans = -1
for i in arr:
    if i == 0: continue

    if max_value < arr[i]:
        max_value = arr[i]
        ans = i
    elif max_value == arr[i]:
        ans = -1

print(ans if ans != -1 else "skipped")