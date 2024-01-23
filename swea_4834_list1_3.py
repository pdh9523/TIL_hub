test_case = int(input()) # 테스트 케이스 설정

for i in range(test_case) :
    card_dict = {} # 값을 담을 딕셔너리 생성
    for k in range(10) :
        card_dict[k] = 0
    
    test_range = int(input()) # N 카드 장수
    card_list = list(input()) # 카드 (여백 없으니 str input을 list로 받아 하나씩 분리)
    
    for j in card_list : # 딕셔너리에 담기
        card_dict[(int(j))] += 1 # 딕셔너리를 int로 만들었으니 바꾼 후 정렬
    
    rem = 0 # 값 비교 (rem에 value, result에 key)
    result = 0
    for key,value in card_dict.items() :
        if value >= rem : # 카드 장수가 비교 대상 이상인 경우
            if key > result : # 카드 숫자가 더 크면
                result,rem = key,value # 담는다
    print(f"#{i+1} {result} {rem}")