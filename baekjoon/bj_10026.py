from collections import deque

t = int(input()) # 그림의 크기를 받음

pic = [list(input()) for _ in range(t)]


# 1) 일반인이 보는 경우
#### RG : 1, B: 2로 바꾸고, 적록색약 기준으로 새롭게 재편

dil = [1,0,-1,0]
djl = [0,1,0,-1]

pic_lst = ["R","G","B"]
normal_cnt = 0
visit = [[0 for _ in range(t+1)] for _ in range(t+1)]
for pix in pic_lst:
    for i in range(t) :
        for j in range(t) :
            if pic[i][j] == pix:
                start = [i,j]
                q = deque()
                q.append(start)

                while q :
                    ti, tj = q.popleft()
                    if pic[ti][tj] == pix :
                        visit[ti][tj] = 1
                        if pix in "RG":
                            pic[ti][tj] = 1
                        else :
                            pic[ti][tj] = 2

                    for idx in range(4) :
                        di = ti + dil[idx]
                        dj = tj + djl[idx]
                        if 0 <= di < t and 0 <= dj < t :
                            if pic[di][dj] == pix and visit[di][dj] == 0 :
                                if pix in "RG":
                                    pic[di][dj] = 1
                                else :
                                    pic[di][dj] = 2
                                q.append([di,dj])
                
                normal_cnt += 1

# 2) 색약이 보는 경우

abnormal_cnt = 0

visit = [[0 for _ in range(t+1)] for _ in range(t+1)]

for modi_pix in range(1,3):
    for i in range(t) :
        for j in range(t) :
            if pic[i][j] == modi_pix:
                start = [i,j]
                q = deque()
                q.append(start)

                while q :
                    ti, tj = q.popleft()
                    if pic[ti][tj] != 0 and pic[ti][tj] == modi_pix :
                        visit[ti][tj] = 1
                    for idx in range(4) :
                        di = ti + dil[idx]
                        dj = tj + djl[idx]
                        if 0 <= di < t and 0 <= dj < t :
                            if pic[di][dj] == modi_pix and visit[di][dj] == 0 :
                                pic[di][dj] = 0
                                q.append([di,dj])
            
                abnormal_cnt += 1

print(normal_cnt, abnormal_cnt)
# 함수 선언할"껄" 34164kb / 108ms