for idx in range(10): # 10개의 테스트 케이스 

    a = int(input()) 
    test_list = list(map(int,input().split()))

    output = 0 
    for i in range(2,len(test_list)-2) : # 앞 뒤 0 을 제외한 범위 설정
        if max(test_list[i-2:i+3]) == test_list[i] : # 앞2 test_list[i] 뒤2 중 최대치가 t[i] 인 경우
            max_list = test_list[i-2:i+3] # 리스트를 설정하는데, 최대치인 i를 remove 하고
            max_list. remove(test_list[i])
            output += (test_list[i] - max(max_list)) # 나머지의 최대치와 t[i]의 차이를 output 에 누적
    print(f"#{idx+1} {output}") 