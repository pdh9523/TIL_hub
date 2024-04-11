import sys

a,b = map(int,input().split())
while not (a==0 and b==0) :
    test_list = []
    test_dict = {}

    for _ in range(a) :
        test_list = list(map(int, sys.stdin.readline().split()))
        for i in test_list :
            test_dict[i] = test_dict.setdefault(i, 0) + 1
        
    sorting_list= list(test_dict.items())
    sorting_list.sort(key= lambda x : x[1], reverse=True)
    result = []
    target = sorting_list[1][1] 
    for idx in range(1, len(sorting_list)) :
        if sorting_list[idx][1] == target :
            result.append(sorting_list[idx][0])
        elif sorting_list[idx][1] < target :
            break
        result.sort()
    print(*result)

    a,b = map(int,input().split())