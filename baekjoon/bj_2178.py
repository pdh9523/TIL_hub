n,m = map(int,input().split())

test_list = [list(input()) for _ in range(n)]

start = (0,0)
end = (n-1,m-1)

visit = []
not_visit = [] 
visit_dict = []
count = 0
count_list = []
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

while True : 
    visit.append(start)
    count += 1
    for delta in range(4) :
        i = start[0] + di[delta]
        j = start[1] + dj[delta]
        if 0 <= i < n and 0 <= j < m :
            if test_list[i][j] == 1 and (i,j) not in visit:
                not_visit.append((i,j))  
                visit_dict[(i,j)] = count
                start = (i,j)
            elif (i,j) == end :
                count_list.append(count)
                