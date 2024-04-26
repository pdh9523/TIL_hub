def backtrack(i=0,j=0, cnt=3):
    global ans 
    # 종료 조건
    if i == N-1 and j == N-1 :
        if target_i or target_j :
            ans = False
        else :
            ans = True
        return
    # 정답 나온 이후 조건은 무시
    if ans :
        return
    
    # 인덱스 변경 조건
    if j == N :
        i,j = i+1,0
        
    check_i, check_j = False, False
    if cnt and school[i][j] == "X":
        if i in target_i or j in target_j :
            if i in target_i :
                target_i.remove(i)
                check_i = True
            if j in target_j :
                target_j.remove(j)
                check_j = True
            backtrack(i,j+1,cnt-1)
            if check_i :
                target_i.append(i)
            if check_j :
                target_j.append(j)


    backtrack(i,j+1,cnt)

N = int(input())

teacher_i = []
teacher_j = []

student_i = []
student_j = []

school = [ input().split() for _ in range(N) ]

for i in range(N):
    for j in range(N):
        if school[i][j] == 'T' :
            teacher_i.append(i)
            teacher_j.append(j)
        if school[i][j] == 'S' :
            student_i.append(i)
            student_j.append(j)

target_i, target_j = [], []

for i in range(len(student_i)):
    if student_i[i] in teacher_i:
        target_i.append(student_i[i])
    if student_j[i] in teacher_j:
        target_j.append(student_j[i])

ans = False

backtrack()
print("YES" if ans else "NO")