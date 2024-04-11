test_dict = {}
length = 0
for i in range(5) :
    a = list(input())
    if len(a) > length :
        length = len(a)
    test_dict[i] = a
for j in range(length) :
    for k in range(5) :
        if j >= len(test_dict[k]) :
            pass
        else :
            print(test_dict[k][j],end="")