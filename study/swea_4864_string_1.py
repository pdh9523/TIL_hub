t = int(input()) #테스트 케이스

for i in range(t) :
    a = input() # 있어야 하는 단어
    a_compare = input() # 비교 문장
    length = len(a) # 단어 길이

    for j in range(len(a_compare)) : # 인덱스를 기준으로 비교 문장을 슬라이싱해 a와 같은지 비교
        if a == a_compare[j:j+length] : # 같으면 1
            print(f"#{i+1} 1") 
            break
    else :
        print(f"#{i+1} 0")


t = int(input())
for i in range(t) :

    test_case = input()
    compare_case = input()

    if test_case in compare_case :
        print(f"{i+1} 1")
    else :
        print(f"{i+1} 0")