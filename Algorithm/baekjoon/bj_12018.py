N,M = map(int,input().split())
# M 마일리지
mileage = []
for _ in range(N):
    P,L = map(int,input().split())  # L 정원
    students = [*map(int,input().split())] 
    if P < L :
        mileage.append(1)
    else :
        students.sort(reverse=True)
        mileage.append(students[L-1])
        
mileage.sort(reverse=True)

cnt = 0

while mileage :
    M -= mileage.pop()
    if M >= 0 :
        cnt += 1
    else : break

print(cnt)