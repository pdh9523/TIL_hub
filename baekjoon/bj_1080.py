def flip(lst,i,j) :
    for a in range(i,i+3):
        for b in range(j,j+3):
            lst[a][b] = 1-lst[a][b]


N,M = map(int,input().split())
A = [list(map(int,list(input()))) for _ in range(N)]
B = [list(map(int,list(input()))) for _ in range(N)]

if N < 3 or M < 3 :     # 1) 주어진 행렬이 3 보다 짧은 경우
    if A!=B :           #    똑같이 생긴게 아니면
        print(-1)       
    else :              #    똑같이 생겼으면
        print(0)
else :
    for i in range(N-2):
        for j in range(M-2):
            if A[i:i+3] == list(map(lambda x: 1-x, B[i:i+3])):  # 이거 좀 고치기

                flip(A,i,j)
print(A)