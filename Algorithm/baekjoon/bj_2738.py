n,m = map(int,input().split())
a = {}
b = {}
output = []
for i in range(n) :
    a[i] = list(map(int,input().split()))
for j in range(n) :
    b[j] = list(map(int,input().split()))

for k in range(n) :
    rem = []
    for l in range(m) :
        rem.append(a[k][l] + b[k][l])
    output.append(rem)
   
for x in range(n) :
    for y in range(m) :
        print(output[x][y], end = " ")
    if x < n-1 :
        print()