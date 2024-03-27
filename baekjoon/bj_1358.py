W,H,X,Y,P = map(int,input().split())
# W : 사각형 너비 
# H : 사각형 높이
# X : x 좌표
# Y : y 좌표

# radius : 반지름
radius = H/2


cnt = 0
for _ in range(P):
    x,y = map(int,input().split())

    # 조건 1) 사각형 안에 들어가있기
    if X <= x <= X+W and Y <= y <= Y+H :
        cnt += 1 

    # 조건 2) 원 안에 들어가기
    # 2-1) 왼쪽 원
    elif (x-X)**2 + (y-(Y+radius))**2 <= radius**2 :
        cnt += 1
    # 2-2) 오른쪽 원
    elif (x-(X+W))**2 + (y-(Y+radius))**2 <= radius**2:
        cnt += 1

print(cnt)