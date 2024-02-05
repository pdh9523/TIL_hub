t = int(input())

for idx in range(t) :
    day = int(input())
    test_list = list(map(int,input().split()))
    total = 0 # 순이익 담을 변수
    while test_list : # 종료 조건 : 리스트가 완전히 비었을 경우
        
        if test_list[0] == max(test_list) :  # 리스트 맨 앞이 리스트의 max값일 경우 pop
            test_list.pop(0) 
            if test_list == [] : # pop 이후 리스트가 비어있으면 아래의 문장에서 Error 발생
                break   # break를 통해 예외처리

        # 매도 시점을 test_list의 최대치 일 때 판매
        sell_time = test_list.index(max(test_list))     

        for i in range(sell_time) :
            total += test_list[sell_time] - test_list[i]

        # 순이익 계산 후, 매도 다음날을 기준으로 리스트 슬라이싱
        test_list = test_list[sell_time+1:] 
    print(f"#{idx+1} {total}")