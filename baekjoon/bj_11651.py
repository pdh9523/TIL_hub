a = int(input())
test_dict = {}
for _ in range(a) :
    x,y = map(int,input().split())

    # y를 key로
    if y not in test_dict :
        test_dict[y] = [x]
    else :
        test_dict[y].append(x)

# y값 정렬
rem = list(test_dict.keys())
rem.sort()

# x값 정렬
for i in rem :
    test_dict[i].sort()

for y_value in rem :
    for x_value in test_dict[y_value] :
        print(f"{x_value} {y_value}")