N,M = map(int,input().split())

# 음수 / 양수 나누기
arr = [*map(int,input().split())]
plus = []
minus = []
for i in arr :
    if i > 0 : plus.append(i)
    elif i < 0 : minus.append(-i)
plus.sort(); minus.sort()

ans = 0 

while plus :
    for i in range(M):
        if plus : 
            a=plus.pop()
            if i == 0 :
                tmp = a
        else : break
    ans += a

    if plus :
        ans += a

ans += a

while minus :
    for i in range(M):
        if minus : 
            a=minus.pop()
            if i == 0 :
                tmp = a
        else : break
    ans += a

    if minus :
        ans += a
print(ans)