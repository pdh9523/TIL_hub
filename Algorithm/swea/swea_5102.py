import sys
sys.stdin = open("5102.txt")

def BFS (S, G, node):
    q = []
    visit = [0] * (node+1)          # 거리에 관한 정보가 담깁니다.

    q.append(S)

    while q :
        tc = q.pop(0)   # 탐색 대상
    
        if tc == G :
            return visit[tc]     # 반환
                                    
        for i in adj_lst[tc] :      # 인접 리스트를 만들었으니 2차원 리스트 내부를 순회합니다.
            if visit[i] == 0 :      # 거리가 0이다 = 아직 방문한 적이 없다.
                q.append(i)
                visit[i] = visit[tc] + 1 # 거리에 관한 정보가 담깁니다.
    return 0




t = int(input())

for i in range(t):
    V,E = map(int,input().split())  # V 노드의 최대값 E 노드의 개수

    adj_lst = [[] for _ in range(V+1)]

    for _ in range(E) :
        # 방향성이 없으므로 양방향으로 인접 리스트 작성
        adj_contents = tuple(map(int,input().split()))      
        adj_lst[adj_contents[0]].append(adj_contents[1])    
        adj_lst[adj_contents[1]].append(adj_contents[0])
    
    S,G = map(int,input().split())  # S 시작점 G 도착점

    result = BFS(S,G,V)

    print(f"#{i+1} {result}")
