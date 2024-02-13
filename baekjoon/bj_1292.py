a, b = map(int,input().split())
test_list = []
for i in range(1,b+1) :
    for _ in range(i) :
        test_list.append(i)
        if len(test_list) >= b :
            break
    if len(test_list) >= b :
            break

print(sum(test_list[a-1:b]))