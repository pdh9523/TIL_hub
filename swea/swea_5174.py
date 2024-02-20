import sys
sys.stdin = open("5174.txt")
from collections import deque


t = int(input())

for idx in range(t):
    E,N = map(int,input().split())
    tr = list(map(int,input().split()))
    max_value = max(tr)                         # 입력된 값 중 최대값을 기준으로 리스트의 크기를 정함
    tree = [[] for _ in range(max_value +1)]
    for i in range(0,len(tr),2):
        tree[tr[i]].append(tr[i+1])             # 입력된 데이터를 처리해 트리 형태로 수정

    q = deque([N])
    visit = [0] * (max_value+1) 
    visit[N] = 1
    while q :
        tc = q.popleft()
        if tree[tc] != []:
            for item in tree[tc]:
                q.append(item)
                visit[item] = 1
    print(f"#{idx+1} {sum(visit)}")         # 1의 개수를 세면 방문한 모든 점(트리가 갈 수 있는 모든 곳 = 잎의 개수)을 알 수 있다.