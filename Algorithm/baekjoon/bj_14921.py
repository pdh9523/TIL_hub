left = 0
right = int(input())-1
arr = sorted([*map(int,input().split())])

ans = 0
tmp = float('inf')
while left<right:
    num = arr[left]+arr[right]
    
    if abs(num) < tmp:
        tmp = abs(num)
        ans = num
    
    if num == 0: break

    elif num > 0: right-=1
    else: left+=1

print(ans)