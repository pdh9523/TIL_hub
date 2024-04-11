t =int(input())

test_list = []  # 입력값은 리스트에 담음

for _ in range(t) :
    test_list.append(input()) 

idx = -1 # 뒤로부터 인덱스를 탐색할 것
while True :
    test_set = set()    # 테스트 세트를 정의하고
    for ele in test_list :
        test_set.add(ele[idx:])     # 슬라이싱을 통해 값을 받고, 세트를 통해 중복값 제거
    if len(test_set) == t :     # 중복값이 없는 경우
        break     # while문 중단

    idx-=1    # 중단되지 않으면 idx를 -1 낮춰서 다시 시행
print(abs(idx))     # 인덱스의 절대값을 출력