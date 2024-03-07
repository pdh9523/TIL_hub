import sys
input = sys.stdin.readline

size = int(input().strip())
gomgoms = []
where = []                      # G 있는 좌표
for i in range(size):
    gomgom = list(input().strip())
    for j in enumerate(gomgom):
        if j[1] =="G" :
            where.append((i,j[0]))
    gomgoms.append(gomgom)
        
# 4가지 경우 비교

a = sorted(where, key= lambda x: x[0])
b = sorted(where, key= lambda x: x[1])

x1 = a[0][0]        # 세로최소치
x2 = a[-1][0]       # 세로최대치

y1 = b[0][1]        # 가로최소치
y2 = b[-1][1]       # 가로최대치

x11 = size-1-x1
y11 = size-1-y1

if x1==x2 and y1==y2 :      # 반례 1 (한곳에 모여있다)
    print(0)
elif x1==x2 :               # 반례 2 x 열이 한줄에 모여 있다
    print(min(y11,y2))
elif y1==y2 :               # 반례 3 y 열이 한줄에 모여 있다
    print(min(x11,x2))      
else :                      # 일반적인 경우
    print(min(x11+y11, x2+y11, x11+y2, x2+y2))

# 오른쪽 위로 미는 경우
# y1 채택 size-1-y1
# x2 채택 x2

# 오른쪽 아래로 미는 경우
# y1 채택 size-1-y1
# x1 채택 size-1-x1

# 왼쪽 위로 미는 경우
# y2 채택 y2
# x2 채택 x2
    
# 왼쪽 아래로 미는 경우
# y2 채택 y2
# x1 채택 size-1-x1