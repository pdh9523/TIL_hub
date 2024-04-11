a=int(input()) #테스트 번호
for x in range(a) :
    b=int(input()) #케이스 번호
    test_case=list(map(int,input().split()))
    test_case.sort()

    test_dict ={}
    for i in range(101) :
        test_dict[i]=0
    for j in test_case :
        test_dict[j] += 1
    max_value = 0 # 숫자
    rem = 0 # 개수
    for i in test_dict :
        if test_dict[i] >= rem :
            if i > max_value :
                rem = test_dict[i]
                max_value = i
    print(f'#{b} {max_value}')