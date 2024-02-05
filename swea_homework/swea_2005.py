def factorial(n) : #팩토리얼 정의
    if n <= 1 :
        return 1
    else :
        return n* factorial(n-1)
    
t = int(input())

for i in range(t) :
    test_case = int(input())

    print(f"#{i+1}") # 테케 번호

    print(1) # 1 (0c0 기본값)
    if test_case > 1 : # 1 이상인 경우
        for a in range(1,test_case) :
            for i in range(a+1) : # 각 자리는 nc0 부터 ncn까지 순서대로
                print(int((factorial(a)/factorial(i))/factorial(a-i)), end=" ")
            print()