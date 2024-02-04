a= [
    [1,2,3,4],
    [4,5,6,7],
    [7,8,9,10]
]

for i in range(len(a)) :
    for j in range(len(a[0])) :
        if i % 2 == 0:
            print(a[i][j])
        if i % 2 == 1 :
            print(a[i][len(a[0])-j-1])