def fi(n) :
    result = {-1:1, 0:0, 1:1, 2:1}
    count = 3
    while n >= count :
        result[count] = result[count-1] + result[count-2]
        count+=1
    return result[n]

a = int(input())

for _ in range(a) :
    b = int(input())
    print(fi(b-1), fi(b))