import sys
input = sys.stdin.readline

def init(start, end, idx=1):
    if start==end :
        tree[idx] = arr[start]
    else :
        mid = (start+end) // 2
        tree[idx] = min(init(start,mid,idx*2), init(mid+1,end,idx*2+1))
    return tree[idx]


def find(start,end,idx,left,right):
    if start > right or end < left :
        return float('inf')

    if start >= left and end <= right :
        return tree[idx]
    
    mid = (start + end) // 2
    return min(find(start,mid,idx*2,left,right), find(mid+1,end,idx*2+1,left,right))


N,M = map(int,input().split())
arr = [int(input()) for _ in range(N)]

tree = [0] * (4*N)
init(0,N-1)
for _ in range(M):
    left,right = map(lambda x :int(x)-1,input().split())
    print(find(0,N-1,1,left,right))
print({k:v for k,v in enumerate(tree)})