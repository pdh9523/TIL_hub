t = int(input())

for i in range(t) :
    n,m = map(int,input().split()) # 문제의 N, M 할당
    test_list = [] # 2차원 배열 생성
    for _ in range(n) :
        rem = list(map(int,input().split())) 
        test_list.append(rem)
    # 계산식
    output = 0
    result = [] # 각 케이스에 대해서 최대값을 출력
    for x in range(n-m+1) : # N 배열에서, M 범위까지 잡을 수 있으면 N-M +1을 기준으로 M범위를 잡으면 끝까지 잡을 수 있음
        for y in range(n-m+1) :
            for d in range(m) : # 범위에서
                output += sum(test_list[y+d][x:x+m]) #y+m x+m만큼 다 더함
            result.append(output) # output을 result에 담고 초기화
            output = 0
    print(f"{i+1} {max(result)}") # 최대값 출력