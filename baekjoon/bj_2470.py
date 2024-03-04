t = int(input())

arr = list(map(int,input().split()))
arr.sort()
max_value = 10000000000000
for i in range(t):
    if abs(sum(arr[i:i+2])) < max_value:
        arr[i],arr[i+1]