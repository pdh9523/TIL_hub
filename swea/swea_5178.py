import sys

sys.stdin = open("5178.txt")

t = int(input())

for i in range(t):
    N,M,L = map(int,input().split())
    tree = [0] * (2*N+1)                    # 딱맞게 N+1 로 설정하려 했으나 13번 줄 for문에서 idx*2+1 까지 사용하므로 인덱스 에러 방지를 위해 설정
    for _ in range(M):
        leaf,value = map(int,input().split())
        tree[leaf] = value
    for idx in range(N,0,-1):               # 리프 노드는 아래쪽에 있으므로 뒤에서부터 계산
        if tree[idx] == 0:            
            tree[idx] = tree[idx*2] + tree[idx*2+1]     # 1 - 2,3 / 2 - 4,5 / 3 - 6,7 / 4 - 8,9 ...
    print(f"#{i+1} {tree[L]}")