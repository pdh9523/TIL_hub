N = int(input())
sg = professor = 0

classrooms = []
for i in range(N):
    classroom = list(map(int,input().split()))
    if not professor and 5 in classroom :
        professor = (i,classroom.index(5))
    if not sg and 2 in classroom :
        sg = (i,classroom.index(2))
    
    classrooms.append(classroom)

x1,y1 = professor
x2,y2 = sg

if x1 > x2 : 
    x2,x1 = x1,x2
if y1 > y2 :
    y2,y1 = y1,y2
    
cnt = 0
for i in range(x1,x2+1):
    for j in range(y1,y2+1):
        if classrooms[i][j] == 1:
            cnt += 1

if (x1-x2)**2 + (y1-y2)**2 >= 25 : 
    print(int(cnt>=3))
else :
    print(0)