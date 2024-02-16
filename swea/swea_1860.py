t = int(input())

for i in range(t) :
    N,M,K = map(int,input().split())    # N 인원 M 시간 K 생산량
    buyers = list(map(int,input().split()))
    buyers.sort()   # 순서대로 정렬
    
    for idx in range(N) :
        
        if idx+1 > buyers[idx] // M * K :   # idx+1 은 필요량, 뒤의 식은 구매자가 도착했을때 최대로 생산할 수 있는 붕어빵의 수량
            print(f"#{i+1} Impossible")
            break
    
    else :
        print(f"#{i+1} Possible")