import sys; input = sys.stdin.readline

N = int(input())
arr = [*map(int,input().split())]

root = -1
tree = [[] for _ in range(N)]
for i in range(N):
    if arr[i] == -1: root = i; continue
    tree[arr[i]].append(i)

cut = int(input())
if cut == root: exit(print(0))


ans = 0
stack = [root]
visit = set()
while stack:
    now = stack.pop()
    if now in visit: continue
    if now == cut: continue

    visit.add(now)
    
    if not tree[now] or (cut in tree[now] and len(tree[now])==1): 
        ans += 1
        continue

    for nxt in tree[now]:
        stack.append(nxt)

print(ans)