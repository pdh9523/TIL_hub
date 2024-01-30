t = int(input())
for test_case in range(t) :
    k,n,m = map(int,input().split()) # k 이동 가능 거리
    stop = list(map(int,input().split())) + [n] # 충전소 위치 + 종점 지정
    ping = 0 # 현재 위치
    idx = 0 # 충전소 인덱스 
    count = 0 # 카운트

    test_list = [] # 충전소 간 거리로 지정해서 while 강제탈출 조건으로 만듬
    for i in range(len(m)-1) : 
        test_list.append((m[i+1]-m[i])) 

    while ping < n : 
        if max(test_list) > k : # 1) 충전소 간 거리가 이동 가능 거리보다 길면
            break # 1-1) break 걸고 count 기본값인 0 반환
        
        if stop[idx] == stop[-1] : # 2) 남은게 마지막 정류소면
                ping = stop[-1]  # 도착 (while문 종료조건)
        
        elif stop[idx]-ping <= k < stop[idx+1]-ping : # 3) 메인 비교문
            ping = stop[idx] # 인덱스 사이에 떨어지면 인덱스로 지정
            count+=1 # 카운팅
        idx+=1 # 인덱스 올리기 (인덱스 사이에 떨어지지 않고 더 큰 값에서 떨어지면 카운트는 두고 인덱스만 올려 다시 비교)

    print(f"#{test_case+1} {count}") #출력