N = int(input())

arr = sorted([*map(int,input().split())])

ans = 0
for i in range(N) :
    target = arr[i]
    left = 0
    right = N-1
    while left < right :
        if arr[left]+arr[right] == target :
            if left == i :
                left += 1
            elif right == i : 
                right -= 1
            else : 
                ans += 1
                break
        elif arr[left]+arr[right] > target :
            right -= 1
        elif arr[left]+arr[right] < target :
            left += 1
print(ans)