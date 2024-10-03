def is_distinct(k):
    tmp = set()
    for arr in data:
        if k < len(arr):
            if arr[k] in tmp:
                return False
            tmp.add(arr[k])
    return True

data = []
for _ in range(int(input())):
    data.append([*map(int,input().split())][:-1])

ans = 0
while not is_distinct(ans):
    ans += 1

print(ans+1)