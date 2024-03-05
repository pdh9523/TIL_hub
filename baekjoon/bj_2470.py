t = int(input())

arr = list(map(int,input().split()))
arr.sort()
target = 10000000000000
for i in range(len(arr)):
    for j in range(len(arr)-1,i,-1):
        if abs(arr[i] + arr[j]) <= target:
            target = abs(arr[i] + arr[j])
            ans = (arr[i], arr[j])
        else :
            break
        if target == 0:
            exit(print(*sorted(ans)))

print(*sorted(ans))

# 시간초과

