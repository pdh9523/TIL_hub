import sys
sys.stdin = open("1227.txt")

for _ in range(10) :
    t = int(input())
    test_list = [list(input()) for _ in range(100)]  # split으로 못받음

    for idx in range(len(test_list)) :
        if "2" in test_list[idx] :    # 굳이 int로 돌릴 필요 없이 문자열으로 작업
            start = [idx, test_list[idx].index("2")]
            break

    visit = []
    not_visit = []

    di = [0,1,0,-1]     # 델타 탐색 시행
    dj = [1,0,-1,0]
    result = 0  # 기본 결과값 (False)
    while result == 0 :
        visit.append(start)
        
        for idx in range(4) :
            i = start[0] + di[idx]
            j = start[1] + dj[idx]
            if 0 <= i < 100 and 0 <= j < 100 :
                if test_list[i][j] == "0" :  # visit에 없고 길이 있는 경우
                    test_list[i][j] = "1"
                    not_visit.append([i,j])     # 탐색 대상에 추가
                if test_list[i][j] == "3":  # DFS 시행 중 찾은 경우 result를 1로 지정후 break
                    result = 1
                    break
                
        if not_visit :  # 탐색 대상이 남아 있는 경우
            start = not_visit.pop() # 꺼내서 start로 지정
        else :
            break
    print(f"#{t} {result}")