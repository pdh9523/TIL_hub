N = int(input())


arr = [2, 4]

total = 1

for i in range(N):
    if i > 1 : 
        tmp = arr[i-1]*2 + arr[i-2]
        arr.append(tmp%9901)
    total += arr[i]
print(total%9901)