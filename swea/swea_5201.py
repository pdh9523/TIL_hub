for idx in range(int(input())):
    N,M = map(int,input().split()) # N : 화물 M : 트럭
    cargo = list(map(int,input().split()))
    truck = list(map(int,input().split()))
    cargo.sort(reverse=True); truck.sort(reverse=True)  # 내림차순 정렬

    ans = 0
    while cargo and truck :
        if cargo[0] > truck[0] :    # 화물이 너무 크면
            cargo.pop(0)            # 버림
        else :
            truck.pop(0)            # 그런게 아니면 큰차 = 큰화물 순으로 내보내고
            ans += cargo.pop(0)     # ans에 더함
    print(f"#{idx+1} {ans}")