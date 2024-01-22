a = int(input())
b = int(input())
sosu = []
for i in range(a,b+1) :
    c = []
    for j in range(1,i+1) :
        if i % j == 0 : 
            c.append(i)
    if len(c) == 2 :
        sosu.append(i)
if len(sosu) == 0 :
    print(-1)
else :
    print(sum(sosu))
    print(min(sosu))
