def get_number(idx):
    tmp = arr[idx]
    for i in range(idx+1, min(N, idx+S+1 )):
        if arr[i] > tmp:
            tmp  = arr[i]
            idx = i
    return tmp, idx

N = int(input())
arr = [*map(int,input().split())]
S = int(input())

for i in range(N-1):
    num,idx = get_number(i)

    if idx != i:
        arr.pop(idx)
        arr.insert(i,num)
        S -= (idx-i)
print(*arr)