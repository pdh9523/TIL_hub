def factorial(n) : # 팩토리얼 함수
    rem = {0:1, 1:1, 2:2} # 계산 중복을 피하기 위해 rem 설정
    for i in range(3,n+1) :
        rem[i] = rem[i-1] * i 
        if rem[i] > n : # 최근에 계산된 값이 입력된 숫자를 넘으면 종료
            break
    result = list(rem.values()) # 계산된 값만 result 변수에 저장 후 반환
    return result

a = int(input())
test_list = factorial(a)

# 부분집합 구하기

subset = [ [] ]
for element in test_list:
    checker = False # 체커를 둔 이유 : 밑에 합 계산 조건에서 for 문을 모두 꺼야하는데, 이중 for문을 모두 끄기 위해 checker를 설정
    size = len(subset) 
    for j in range(size) :
        sub = subset[j]+[element] # 일반적인 부분집합 생성 과정에서, sub 변수로 꺼내서 저장
        subset.append(sub)
        if len(sub) >= 1 : # 길이 1이상인 경우를 판단 (문제조건)
            if sum(sub) == a : # 합이 입력된 숫자와 같다면
                print("YES") # 출력
                checker = True # 체커를 True로 두고 break
                break
            elif sum(sub) > a:
                print("NO")
                checker = True
                break
    if checker : # 만약 위의 if 문에서 break가 되었으면 바깥의 for문도 break
        break