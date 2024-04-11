left = 0
right = int(input()) -1


arr = sorted(list(map(int,input().split())))
min_value = float('inf')
while left < right :
    tmp = abs(arr[right] + arr[left])
    if min_value > tmp:
        min_value = tmp
        ans = [arr[left],arr[right]]
        if tmp == 0 :
            break
    if arr[right] + arr[left] > 0 :
        right -= 1
    else : 
        left += 1
        
print(*ans)