# x,y좌표 비교 최대 최소 출력

t = int(input())
test_list = [[],[]]
for _ in range(t) :
    x,y= map(int,input().split())
    test_list[0].append(x)
    test_list[1].append(y)

x_max = max(test_list[0]) - min(test_list[0]) + 10
y_max = max(test_list[1]) - min(test_list[1]) + 10

x_min = max(test_list[0]) - min(test_list[0]) - 10
y_min = max(test_list[1]) - min(test_list[1]) - 10

if x_min <= 0 or y_min <= 0 :
    print((x_max+y_max)*2)
else :
    print((x_max+y_max+x_min+y_min)*2)