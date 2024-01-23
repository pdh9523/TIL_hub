t = int(input())
for test_case in range(t) :
    k,n,m = map(int,input().split()) # k 이동 가능 거리
    m = list(map(int,input().split())) + [n]
    ping = 0 # 현재 위치 지정
    idx = 0 # 인덱스 세는 렘 
    count = 0 # 카운트

    test_list = [] # 1) 충전소 간 거리가 이동 가능 거리보다 길면 
    for i in range(len(m)-1) :
        test_list.append((m[i+1]-m[i]))

    while ping < n :
        if max(test_list) > k : # 1-1) break 걸고 count 기본값인 0 반환
            break
        if m[idx] == m[-1] : # 2) 남은게 마지막 정류소면
                ping = m[-1]  # 도착 (while문 끝낼 수 있게)
        elif m[idx]-ping <= k < m[idx+1]-ping : # 3) 메인 비교문
            ping = m[idx] # 인덱스 사이에 떨어지면 인덱스로 지정
            count+=1 # 카운팅
        idx+=1 # 인덱스 올리기

    print(f"#{test_case+1} {count}") #출력