from pprint import pprint as print
t = int(input())

for test_case in range(t) :
    color_list = [[0 for _ in range(11)] for _ in range(11)] # 2차원 리스트를 만듭니다. (1번부터 적기 쉬우라고 한칸 더 만듬)

    tt = int(input()) # 색칠 횟수
    for j in range(tt) :
       x1,y1,x2,y2,col = map(int,input().split()) # 순서대로 x,y 좌표 x,y 좌표 색깔

       for y in range(y1,y2+1) :  
           for x in range(x1,x2+1) : # 좌표마다
                if color_list[x][y] == 0 or color_list == col : # 칠하려는 곳이 0이거나, 색이 같은 영역이면
                    color_list[x][y] = col # 색깔로 칠하기
                else : 
                   color_list[x][y] = 3 # 아니면(다른 색이 칠해져 있으면) 3으로
    output=0
    for i in color_list : # 모든 리스트에서
        output+=i.count(3) # 3 갯수 구해서 output에 더하기 
    print(color_list)
    print(f"#{test_case+1} {output}")