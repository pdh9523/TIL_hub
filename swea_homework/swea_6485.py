t = int(input()) # 테스트 케이스 개수

for i in range(t) : 
    test_case = int(input()) # 각 테스트 케이스
    bus_list = [0 for x in range(5001)] # 버스 노선 리스트 (1<=a<=b<=5000 이니까 index 5000번 까지 만들어봄)
    for _ in range(test_case) : # 버스 노선 확인
        a,b = map(int,input().split()) 
        for idx in range(a,b+1) : 
            bus_list[idx] += 1 # a부터 b까지 1 추가 (간다는 뜻)

    p = int(input()) 
    result = []
    for __ in range(p) :
        result.append(bus_list[int(input())]) # p이후 각 입력에 대한 정류장의 값을 확인하니까 입력할때마다 리스트에 담아서

    print(f"#{i+1}", *result) # 언패킹