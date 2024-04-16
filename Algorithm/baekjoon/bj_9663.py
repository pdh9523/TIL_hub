import time

a=  time.time()
def backtracking(i=0):
    global ans
    for j in range(N):
        if queen(i,j): # 유망하면
            board[i] = j
            if i == N-1: #다 놓았다면
                ans += 1
                return
            else:
                backtracking(i+1)

def queen(i,j): #유망 조건
    for a in range(i):
        if board[a] == j or abs(board[a]-j) == abs(a-i): # 같은 열이거나 같은 대각선
            return False 
    return True 

N = int(input())

board = [0] *N 
ans = 0
backtracking()
print(ans)

print(time.time()-a)