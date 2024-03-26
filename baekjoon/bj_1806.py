N,S = map(int,input().split())

arr = list(map(int,input().split()))

left = 0
right = 0
cnt = []
sums = arr[left]
while left != N and right <= N-1:
    if sums >= S :
        if right == left :
            exit(print(1))
        else :
            cnt.append(right-left+1)
        sums -= arr[left]
        left += 1
    else :
        if right < N-1:
            right += 1
            sums += arr[right]
        else:
            break 
if cnt :
    print(min(cnt))
else :
    print(0)