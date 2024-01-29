t = int(input())

for i in range(t) :
    n,k = map(int,input().split())  # 문제의 N,K 할당
    test_list = []
    for _ in range(n) :
        test_list.append((input().split()))
    
    output = 0 
    # x열 확인
    for arr in test_list : 
        output += list(map(len,"".join(arr).split("0"))).count(k)
    # x열은 리스트 하나로 뽑아낼 수 있으니까 join으로 합친 후 0으로 스플릿, 1의 길이를 재서 k와 같은경우 count에 더함
    
    # y열 확인
    char = ""
    for x in range(n) :
        for y in range(n) :
            char += test_list[y][x] 
        output += list(map(len,char.split("0"))).count(k)
        char = ""
    # y는 x y열에서 세로로 1개씩 꺼내서 char문자열 하나를 만듬. 이후는 x열 비교와 동일
    print(f"#{i+1} {output}")