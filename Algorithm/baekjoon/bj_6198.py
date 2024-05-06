import sys

input = sys.stdin.readline


bd = [int(input()) for _ in range(int(input()))]
stack = []
ans = 0
cnt = 0
for i in bd :
    while stack and stack[-1] <= i :
        stack.pop()
        cnt -=1
    stack.append(i)
    cnt += 1

    ans += cnt-1

print(ans)