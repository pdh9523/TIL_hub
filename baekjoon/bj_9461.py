def pado(n):
    result = {1:1,2:1,3:1,4:2,5:2}
    for i in range(6,n+1) :
        result[i] = result[i-1] + result[i-5]
    return result[n]

a = int(input())

for _ in range(a) :
    print(pado(int(input())))