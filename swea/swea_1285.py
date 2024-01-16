test_case = int(input()) #테스트 케이스
for i in range(test_case) :
    test_number = int(input()) #인원수
    test_range = list(map(int,input().split()))
    test_dict = {}
    for j in test_range :
        if test_dict[j] not in test_dict :
            test_dict[j] = 1
        else :
            test_dict[j] +=1
    print(test_dict)
    