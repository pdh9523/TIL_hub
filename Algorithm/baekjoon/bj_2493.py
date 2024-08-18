N = int(input())
arr = [*map(int,input().split())]
ans = [0]*N
stack = []
for i in range(N):
    while stack:
        if arr[i]>arr[stack[-1][0]]:
            stack.pop()
        else:
            ans[i] = stack[-1][0]+1
            break
    stack.append((i,arr[i]))
print(*ans)