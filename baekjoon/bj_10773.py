a = int(input())
jaemin_list = []
for i in range(a) :
    test_case = int(input())
    if test_case == 0 :
        jaemin_list.pop()
    else :
        jaemin_list.append(test_case)
print(sum(jaemin_list))