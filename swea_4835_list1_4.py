t = int(input()) # 테스트 케이스 설정

for i in range(t) :
    n,m = map(int,input().split()) #구간과 개수 설정
    test_list = list(map(int,input().split())) # 리스트로 변환

    modi_list = [] # 구간합 자체를 새로운 리스트로 생성
    for j in range(n-m+1) : # 10을 3개씩 묶으면 10-3+1 = 8 개의 원소가 생김
        element=0
        for k in range(m) : # 부분합 구하기
            element+= test_list[j+k] # j에서 시작해서 m개 만큼 더하기
        modi_list.append(element) # 구간합 리스트에 담기
    
    print(f"#{i+1} {max(modi_list)-min(modi_list)}") # 최대 - 최소 출력