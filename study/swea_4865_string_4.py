t = int(input()) # 테스트 케이스 입력

for i in range(t) :
    a = input() # 단어 입력

    a_dict = {} # 단어에 기반한 비교 딕셔너리 생성
    for char in a :
        if char not in a_dict :
            a_dict[char] = 0 

    a_compare = input() # 비교 문자열 입력

    for j in a_compare : # 문자열의 각 값이 딕셔너리에 있으면 +1 
        if j in a_dict.keys() :
            a_dict[j] += 1

for i in range(t) :
    test_case = input()

    test_dict = {}
    for char in test_dict :
        test_dict.setdefault(char, 0)

    compare_case = input()

    for char in compare_case :
        if char in test_dict :
            test_dict[char] += 1

    result = max(test_dict.values()) # value 중 최대값
    print(f"#{i+1} {result}") # 출력