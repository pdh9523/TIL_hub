from collections import deque

N,t = int(input()), int(input())

students = deque(map(int,input().split()))

pic = deque()

star = [0] * 101

while students:
    student = students.popleft()
    star[student] +=1
    if student not in pic :
        if len(pic) < N:
            pic.append(student)
        else:
            min = 1000
            for i in pic:
                if star[i] < min :
                    min = star[i]
                    target = i
            pic.remove(target)
            star[target] = 0
            pic.append(student)
print(*sorted(pic))