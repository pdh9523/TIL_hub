def putCandy(left, right, node, b, c):
    tree[node] += c
    if left == right:
        return    
    mid = (left+right) // 2
    if b <= mid:
        putCandy(left, mid, node*2, b, c)
    else:
        putCandy(mid+1, right, node*2+1, b, c)


def findCandy(left, right, node, b):
    tree[node] -= 1
    if left == right:
        return left
    mid = (left+right) // 2
    if tree[node*2] >= b:
        return findCandy(left, mid, node*2, b)
    else:
        return findCandy(mid+1, right, node*2+1, b-tree[node*2])


# N: 손을 댄 횟수
tree = [0]*(4*10**6)

N = int(input())
for _ in range(N):
    cmd, *items = map(int,input().split())
    if cmd == 1:
        print(findCandy(1, 10**6, 1, items[0]))
    else:
        putCandy(1, 10**6, 1, items[0], items[1])