def inorder(now):
    global num
    if 0 < now <= N:
        inorder(tree[now][1])
        tree[now][0] = num
        print(tree)
        num += 1
        inorder(tree[now][2])

for tc in range(int(input())):
    N = int(input())
    tree = [[0, 2*i, 2*i+1] for i in range(N+1)]
    num = 1
    inorder(1)
    print(f'#{tc+1} {tree[1][0]} {tree[N//2][0]}')