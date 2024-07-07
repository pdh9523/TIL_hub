import sys
input = sys.stdin.readline

def init(start,end,idx=1):
    if start==end:
        tree[idx] = arr[start-1]
    else:
        mid = (start+end)//2
        tree[idx] = init(start,mid,idx*2) + init(mid+1,end,idx*2+1)
    return tree[idx]

def find(start,end,idx,left,right):
    if start > right or end < left:
        return 0
    
    if start >= left and end <= right:
        return tree[idx]

    mid = (start+end)//2
    return find(start,mid,idx*2,left,right) + find(mid+1,end,idx*2+1,left,right)

def update(start,end,idx,new_idx,data):
    if start > new_idx or end < new_idx: return
    tree[idx] += data

    if start == end: return

    mid = (start+end)//2
    update(start,mid,idx*2, new_idx,data)
    update(mid+1,end,idx*2+1, new_idx,data)

N,M,K = map(int,input().split())
arr = [int(input()) for _ in range(N)]

tree = [0]*(4*N)

init(1,N)
for _ in range(M+K):
    a,b,c = map(int,input().split())
    if a==1:
        data = c-arr[b-1]
        arr[b-1]=c
        update(1,N,1,b,data)
    else :
        print(find(1,N,1,b,c))