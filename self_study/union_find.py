# 1~6번까지 노드가 존재
# 1. make_set
def make_set(n):
    return[i for i in range(n)]
# 1~6번까지 사용하기 위해 7번까지 생성
parents = make_set(7)
rank= [0] * 7
print(parents)

# 2. find_set : 대표자 찾기
# 부모 노드를 보고, 부모 노드도 연결이 되어 있다면 다시 반복
# 언제까지? 자기 자신이 대표인 데이터를 찾을 때 까지
def find_set(x):
    # 자기 자신이 대표 ? 끝
    if parents[x] != x:
        parents[x] = find_set(parents[x])

    return parents[x]

def union(x,y):
    root_x = find_set(x)
    root_y = find_set(y)

    # 이미 같은 집합이라면 넘어감
    if root_x != root_y:
        if rank[root_x] < rank[root_y]:
            parents[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parents[root_y] = root_x

        else:
    
    # 다른 집합이면 합침
    if x<y :
        parents[y] = x
    else :
        parents[x] = y