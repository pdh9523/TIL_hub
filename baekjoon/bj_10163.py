import sys

board = [[0] * 1001 for _ in range(1001)]

t = int(input())

for k in range(1,t+1):
    i,j, i_length, j_length = map(int,sys.stdin.readline().strip().split())
    
    for idx in range(i,i+i_length):
        for jdx in range(j,j+j_length):
            board[idx][jdx] = k

for a in range(1,t+1):
    output = 0 
    for b in range(1001):
        output += board[b].count(a)
    print(output)