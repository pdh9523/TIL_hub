# 10 : 1 / 20 : 3 / 30 : 5 (10*2 + 20+1) / 40 : 3*2 + 5*1 /   
rem = [1,3] # 초기값을 넣어두고 그 이상의 테스트 케이스가 들어온 경우 계산한다.
t = int(input())
for idx in range(t) :
    test_case = int(input())//10 # 테스트 케이스를 10으로 나누어 받음

    # 이전 테스트 케이스에서 이미 계산한 경우 그 결과값을 바로 출력한다.
    if len(rem) < test_case: 
        for i in range(len(rem),test_case) : # 렘의 길이 이상의 값이 들어온 경우 계산을 시작한다.
            rem.append(rem[i-1]+2*rem[i-2]) 
    print(rem)    
    print(f"#{idx+1} {rem[test_case-1]}") # 인덱스를 기준으로 하니까 -1의 인덱스를 호출