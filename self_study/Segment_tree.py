# 일반적인 함수는 query, init, find, update로 구성
# 세그먼트 트리는 이진트리를 활용해 각 트리의 가지에 위치 구간별 값을 저장하는 방식으로 이루어진다.

def query(d1,d2):       # 특정 쿼리에 따라 행동하게 된다.
    return d1+d2        # 예시로 구간 합을 구한다면, 각각의 합을 넣어주면 된다.


def init(start,end,idx):
    if start==end:
        tree[idx]=arr[idx]

    else:
        mid = (start+end)//2
        return query(init(start,mid,idx*2),init(mid+1,end,idx*2+1))

def find(start,end,idx,left,right):
    if start > right or end < left:
        return 0                        # 여기의 리턴값도 생각해야함 (쿼리에 변화가 생기지 않는 값으로)

    if start >= left and end <= right:
        return tree[idx]
    
    mid = (start+end)//2
    return query(find(start,mid,idx*2,left,right), find(mid+1,end,idx*2+1,left,right))

def update(start,end,idx,new_idx,data):
    if start > new_idx or end < new_idx: return

    tree[idx] += data
    if start==end: return
    
    # 현재 인덱스의 값을 수정했다면 아래로 재귀
    mid = (start+end)//2
    update(start,mid,idx*2, new_idx,data)   
    update(mid+1,end,idx*2+1,new_idx,data)



N,M = map(int,input().split())
arr = [*map(int,input().split())]
tree = [0]*(4*N)

for _ in range(M):
    
    a,b,c = map(int,input().split())

    if a == "find":
        print(find(1,N,1,b,c))
    
    if a == "update":
        data = c-arr[b]           # 새로운 데이터를 처리 후 update (구간합에서의 새 데이터는 새로운 데이터와 원본데이터 값의 차이)
        arr = c                   # 원 배열에서도 특정 값으로 update
        update(1,N,1,b,data)