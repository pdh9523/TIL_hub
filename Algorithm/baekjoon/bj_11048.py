N,M = map(int,input().split())

maze = [ [*map(int,input().split())] for _ in range(N) ]
DP = [ [0] * M for _ in range(N) ] 
for i in range(N) :
    for j in range(M) :
        if i > 0 and j > 0:
            maze[i][j] += max(maze[i-1][j],maze[i][j-1],maze[i-1][j-1])
        elif j == 0 and i > 0  :
            maze[i][j] += maze[i-1][j]
        elif i == 0 and j > 0  :
            maze[i][j] += maze[i][j-1]
print(maze[-1][-1])