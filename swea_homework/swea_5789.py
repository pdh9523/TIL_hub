t = int(input())

for idx in range(t) :
    n,q = map(int,input().split()) #문제의 N, Q 설정
    test_list = [0 for _ in range(n)] # N개의 0이 적힌 상자
    for i in range(1,q+1) : # i = 1일때부터 시작해서 q일때까지 반복
        l,r = map(int,input().split()) 
        for idx in range(l-1,r) :# L부터 R까지 색칠(인덱스 기준 한칸씩 미룸)
            test_list[idx] = i 
    print(f"#{idx+1}", *test_list) # 언패킹