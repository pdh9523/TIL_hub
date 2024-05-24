from collections import deque

for _ in range(int(input())):
    N = int(input())
    tree = sorted([*map(int,input().split())], reverse=True)
    arr = deque()
    while tree :
        arr.appendleft(tree.pop())
        if tree :
            arr.append(tree.pop())
    ans = 0        
    for i in range(N):
        ans = max(ans, abs(arr[i]-arr[i-1]))
    print(ans)