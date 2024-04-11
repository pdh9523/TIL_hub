t = int(input())
b = list(map(int,input().split()))
count =0
for j in b :
    c = []
    for i in range(1,j+1) :
        if j % i == 0 : 
            c.append(i)
    if len(c) == 2 :
        count += 1
print(count)