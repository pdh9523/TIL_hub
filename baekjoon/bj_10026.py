from collections import deque

t = int(input()) # 그림의 크기를 받음

pic = [list(input()) for _ in range(t)]


# 1) 일반인이 보는 경우
#### 0 1로 바꾸고, 적록색약 기준으로 새롭게 재편해야함
dil = [1,0,-1,0]
djl = [0,1,0,-1]
pic_lst = ["R","G","B"]
blind_lst = ["RG","B"]
normal_cnt = 0
visit = [[0 for _ in range(t+1)] for _ in range(t+1)]
for pix in pic_lst:
    for i in range(t) :
        for j in range(t) :
            start = [i,j]
            q = deque()
            q.append(start)
            count =0
            while q :
                ti, tj = q.popleft()
                if pic[ti][tj] == pix :
                    pic[ti][tj] = 0
                    visit[ti][tj] = 1
                for idx in range(4) :
                    di = ti + dil[idx]
                    dj = tj + djl[idx]
                    if 0 <= di < t and 0 <= dj < t :
                        if pic[di][dj] == pix and visit[di][dj] == 0 :
                            q.append([di,dj])
                            count += 1

            if count > 0 :
                normal_cnt += 1

abnormal_cnt = 0
visit = [[0 for _ in range(t+1)] for _ in range(t+1)]
for pix in pic_lst:
    for i in range(t) :
        for j in range(t) :
            start = [i,j]
            q = deque()
            q.append(start)
            count = 0
            while q :
                ti, tj = q.popleft()
                if pic[ti][tj] != 0 and pic[ti][tj] in pix :
                    pic[ti][tj] = 0
                    visit[ti][tj] = 1
                for idx in range(4) :
                    di = ti + dil[idx]
                    dj = tj + djl[idx]
                    if 0 <= di < t and 0 <= dj < t :
                        if pic[di][dj] != 0 and pic[di][dj] in pix and visit[di][dj] == 0 :
                            q.append([di,dj])
                            count += 1

            if count > 0 :
                abnormal_cnt += 1

print(normal_cnt, abnormal_cnt)