N = int(input())

arr = [*map(int,input().split())]
brr = [*map(int,input().split())]
if arr==brr: exit(print(1))
for i in range(N-1,0,-1):
    for j in range(i-1,-1,-1):
        if arr[i] < arr[j]:
            arr[i],arr[j] = arr[j], arr[i]
            if arr == brr: exit(print(1))
            break
print(0)

N =int(input())

arr = [*map(int,input().split())]
brr = [*map(int,input().split())]

for i in range(N-1,0,-1):
    if arr==brr:
        break
    idx = arr.index(max(arr[:i+1]))
    if idx !=i:
        arr[idx],arr[i] = arr[i], arr[idx]
print(1 if arr==brr else 0)