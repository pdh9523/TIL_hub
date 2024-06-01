def d(n):
    n = str(n)
    result = int(n)
    for i in n :
        result += int(i)
    return result

arr = list(range(10001))

for i in range(10001) :
    if arr[i] == 0 : continue

    tmp = i
    while tmp <= 10000 :
        tmp = d(tmp)
        if tmp <= 10000:
            arr[tmp] = 0
    
for i in arr :
    if i != 0 :
        print(i)