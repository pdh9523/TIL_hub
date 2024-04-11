a = list(map(int,input().split()))

target = [1,1,2,2,2,8]

for i in range(len(a)) :
    target[i] = target[i] - a[i]

for j in target :
    print(j, end=" ")