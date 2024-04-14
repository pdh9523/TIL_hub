import sys

input = sys.stdin.readline

N = int(input())

stack = [] 

ans = [] 

cnt = 1 
for _ in range(N):
    num = int(input())

    while cnt <= num :
        stack.append(cnt)
        ans.append("+")
        cnt += 1
    
    if stack[-1] == num : 
        stack.pop()
        ans.append("-")
    else :
        exit(print("NO"))

print(*ans, sep="\n")