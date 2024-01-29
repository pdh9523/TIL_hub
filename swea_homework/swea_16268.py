t = int(input()) #총 테스트 케이스 개수

for idx in range(1,t+1) : # 테스트 케이스 idx번째로 표현 
    n,m = map(int,input().split()) # 문제의 n,m 변수 차용

    test_list = [[0 for x in range(m+2)]] 
    for i in range(n) :
        test_list.append([0,*map(int,input().split()),0]) #test_list를 2차원 리스트로 활용
    
    test_list.append([0 for x in range(m+2)])

    # 1차 풀이에서, 모서리에 큰 값이 있는 경우 반례가 발생합니다.
    # 그래서, [[100,1,100],[1,1,1],[100,1,100]] 의 경우를 무시하고 통과 하는 경우가 발생합니다.
    # 이를 해결하고자 주어진 차원의 리스트 겉에 0을 붙여 편하게 계산 하려고 리스트를 새로 짰습니다.


    result_list = [] # 각 결과를 합해 max로 표현하기 위해 리스트 활용
    for x in range(1,n) : 
        for y in range(1,m) : # 각 x,y 좌표에서 십자모양으로 더함
            summary = test_list[x][y] + test_list[x-1][y] + test_list[x+1][y] + test_list[x][y+1] + test_list[x][y-1]
        
            result_list.append(summary)
    print(f"{idx} {max(result_list)}")