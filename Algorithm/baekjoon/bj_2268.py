import sys
input = sys.stdin.readline

def find(start,end,idx,left,right):
    if start > right or end < left:
        return 0
    
    if start >= left and end <= right:
        return tree[idx]
    
    mid = (start+end)//2
    return (find(start,mid,idx*2,left,right) + 
            find(mid+1,end,idx*2+1,left,right))

def update(start,end,idx,new_idx,data):
    if start > new_idx or end < new_idx: return
    tree[idx] += data
    if start == end : return

    mid = (start+end)//2
    update(start,mid,idx*2,new_idx,data)
    update(mid+1,end,idx*2+1,new_idx,data)


N,M = map(int,input().split())
arr = [0]*(N+1)

tree = [0]*(4*(N+1))

## init 필요없을듯

for _ in range(M):
    a,b,c = map(int,input().split())
    if a == 0:
        if b>c: c,b=b,c
        print(find(1,N,1,b,c))
    else:
        data = c-arr[b]
        arr[b]=c
        update(1,N,1,b,data)