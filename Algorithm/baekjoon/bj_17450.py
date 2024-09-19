arr = []
for i in range(3):
    price, weight = map(int,input().split())
    if i==0:
        a = "S"
    elif i==1:
        a = "N"
    else:
        a ="U"
    
    price *= 10
    weight *= 10

    if price >= 5000:
        price -= 500
    
    res = weight / price

    arr.append((res,a))
arr.sort(reverse=True)
print(arr[0][1])