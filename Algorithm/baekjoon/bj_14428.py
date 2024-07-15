def init(start,end,idx):
    if start==end:
        tree[idx] = arr[start]
    
    else: 
        mid = (start+end)//2
        tree[idx] = min(init(start,mid,idx*2),init(mid+1,end,idx*2+1))
    return tree[idx]
    
def find(start,end,idx,left,right):
    if start>right or end<left:
        return float('inf')
    
    if start>=left and end<=right:
        return tree[idx]
    
    mid = (start+end)//2
    return min(find(start,mid,idx*2,left,right),find(mid+1,end,idx*2+1,left,right))

def update(start,end,idx,new_idx,data):
    if start>new_idx or end<new_idx: return
    tree[idx] = min(tree[idx],data)
    if start==end: return

    mid = (start+end)//2
    update(start,mid,idx*2,new_idx,data)
    update(mid+1,end,idx*2+1,new_idx,data)


N = int(input())
arr = [*map(int,input().split())]
tree = [0]*4*N
init(0,N-1,0)
for _ in range(int(input())):
    a,b,c = map(int,input().split())

    if a == 1:
        if arr[b]
        update(0,N-1,0,b-1,c)
    else:
        print(find(0,N-1,0,b-1,c-1))