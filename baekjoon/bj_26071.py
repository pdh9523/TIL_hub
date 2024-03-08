import sys
input = sys.stdin.readline

size = int(input().strip())
where = []                      # where : G 있는 좌표
for i in range(size):
    for j in enumerate(list(input().strip())):
        if j[1] =="G" :
            where.append((i,j[0]))
        
x = sorted(where, key= lambda x: x[0])
y = sorted(where, key= lambda x: x[1])

x1,x2 = x[0][0],x[-1][0]        #세로/ x1 : 최소치 x2 : 최대치
y1,y2 = y[0][1],y[-1][1]        #가로/ y1 : 최소치 y2 : 최대치

x11,y11 = size-1-x1, size-1-y1   # 최소치는 size-1에서 뺀 값으로 보정해야함

if x1==x2 and y1==y2 :          # 반례 1 (한곳에 모여있다)
    print(0)
elif x1==x2 :                   # 반례 2 x 열이 한줄에 모여 있다
    print(min(y11,y2))
elif y1==y2 :                   # 반례 3 y 열이 한줄에 모여 있다
    print(min(x11,x2))      
else :                          # 일반적인 경우
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