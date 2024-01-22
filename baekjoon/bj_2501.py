a,b = map(int,input().split())
c = []
for i in range(1,a+1) :
    if a % i == 0 : 
        c.append(i)
if len(c) >= b :
    print(c[b-1])
else :
    print(0)