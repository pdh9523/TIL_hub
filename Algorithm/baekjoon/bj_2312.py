import sys
t = int(input())
for _ in range(t) :
    test_case = int(sys.stdin.readline())
    div = 2
    div_list = list(range(1,test_case+1,2))
    test_dict = {}
    while test_case > 1 :
        if test_case % div == 0 :
            test_case = test_case / div
            test_dict[div] = test_dict.setdefault(div, 0) + 1
             
    for result in test_dict.items() :
        print(*result)