import sys
input = sys.stdin.readline

N = int(input())
stack = []

for _ in range(N):
    stack.append(int(input()))

bottom = max(stack)

cnt = 0
for i in range(N-1,-1,-1):

    if stack[i] == bottom:
        cnt = 1

    elif stack[i] == bottom - cnt:
        cnt+=1
        
print(N-cnt)