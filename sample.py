def inorder(now):
    if 0 < now <= N:
        inorder(tree[now][0])
        global num; tree[now][1] = num; num += 1
        inorder(tree[now][1])

for tc in range(int(input())):
    N = int(input())
    tree = [[2*i, 2*i+1] for i in range(N+1)]
    print(tree)
    num = 1
    inorder(1)
    print(f'#{tc+1} {tree[1][0]} {tree[N//2][0]}')