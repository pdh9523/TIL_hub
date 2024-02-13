N,M = map(int,input().split())


test_list = [list(input()) for _ in range(N)]

for idx in range(N) :
    for jdx in range(M) :
        if test_list[idx][jdx] == "I" :
            start = (idx, jdx)

visit = []
not_visit = [start]

di = [1,0,-1,0]
dj = [0,1,0,-1]
count = 0
while not_visit :
    start = not_visit.pop()
    if test_list[start[0]][start[1]] == "P" :
        count += 1
    test_list[start[0]][start[1]] = "X"
    for dlt in range(4) :
        i = start[0] + di[dlt]
        j = start[1] + dj[dlt]
        if 0<= i < N and 0<= j < M :
            if test_list[i][j] == "O" or test_list[i][j] =="P" :
                not_visit.append((i,j))
if count != 0 :
    print(count)
else :
    print("TT")