# 1 상 2 하 3 좌 4 우
from pprint import pprint 

for idx in range(int(input())):

    N,M,K = map(int,input().split())
    lab = [[[] for _ in range(N)] for _ in range(N)]

    for _ in range(K):
        a,b,c,d = map(int,input().split())
        lab[a][b].append([c,d,0])     # 미생물 수, 이동방향, 0은 체커

    for r in range(M):  # M 만큼의 로테이션 동안
        pprint(lab)
        for i in range(N):
            for j in range(N):
                while lab[i][j] :
                    item = lab[i][j].pop()
                    if item[2] == r :           # 다들 움직여야되니까 한칸씩 다 움직이는거 체크
                        if item[1] == 1 :
                            di, dj = i-1, j
                        elif item[1] == 2:
                            di, dj = i+1,j
                        elif item[1] == 3:
                            di, dj = i,j-1
                        elif item[1] == 4:
                            di, dj = i, j+1

                        if 0 < di < N-1 and 0 < dj < N-1 :
                            lab[di][dj].append([item[0],item[1],item[2]+1])
                        else :
                            if item[1] %2 == 0:
                                item[1] -=1
                            else :
                                item[1] += 1
                            lab[di][dj].append([item[0]//2, item[1], item[2]+1])
        # # 합치기
        # sums=0
        # max_value = 0
        # dr = 0 
        # for i in range(N):
        #     for j in range(N):
        #         if len(lab[i][j]) > 1 :
        #             for ind in range(len(lab[i][j])) :
        #                 if lab[i][j][ind][0] > max_value :
        #                     dr = lab[i][j][ind][1]
        #                 sums += lab[i][j][ind][0]
        #             lab[i][j]=[[sums,dr,lab[i][j][0][2]]]