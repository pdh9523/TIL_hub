t = int(input()) #총 테스트 케이스 개수

for idx in range(1,t+1) : # 테스트 케이스 idx번째로 표현 
    n,m = map(int,input().split()) # 문제의 n,m 변수 차용

    test_list = [[0 for x in range(m+2)]] 
    for i in range(n) :
        test_list.append([0,*map(int,input().split()),0]) #test_list를 2차원 리스트로 활용
    
    test_list.append([0 for x in range(m+2)])

    result_list = [] # 각 결과를 합해 max로 표현하기 위해 리스트 활용
    for x in range(1,n) : 
        for y in range(1,m) : # 각 x,y 좌표에서 십자모양으로 더함
            summary = test_list[x][y] + test_list[x-1][y] + test_list[x+1][y] + test_list[x][y+1] + test_list[x][y-1]
        
            result_list.append(summary)
    print(f"{idx} {max(result_list)}")