def dnc(n, x=0, y=0):
    global white, blue
    col = arr[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if col != arr[i][j]:
                t=n//2
                for dx,dy in (0,0),(0,t),(t,0),(t,t) : dnc(t,x+dx,y+dy)
                return
    if col : blue+=1
    else : white+=1

N = int(input()) 
arr = [[*map(int,input().split())] for _ in range(N)]
white,blue = 0,0
dnc(N)

print(white)
print(blue)