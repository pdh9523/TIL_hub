import sys

input = sys.stdin.readline


N = int(input())
stack = []
ans = 0  
for _ in range(N):
    task, *info = map(int,input().split())
    
    if task == 1 :
        stack.append(list(info))
    if stack :
        stack[-1][1] -= 1
        if stack[-1][1] == 0 :
            ans += stack.pop()[0]
print(ans)