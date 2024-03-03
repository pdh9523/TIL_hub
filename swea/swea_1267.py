for t in range(1,11):
    V,E = map(int,input().split())  # V 정점 E 간선


    required = [[] for _ in range(V+1)]             # required : 선행조건
    tree = [[] for _ in range(V+1)]                 # tree : 트리
    visit = [0] * (V+1)                             # visit : 방문 체크 리스트


    data = list(map(int,input().split()))           # data : 제공된 원 데이터
    for i in range(0,len(data),2):                  # data를 기반으로 트리와 선행조건을 가공
        tree[data[i]].append(data[i+1])             # 트리 (짝수번째 값을 인덱스로 하여 홀수번째 값을 리스트 안에 가지고 있음)
        required[data[i+1]].append(data[i])         # 역행된 선행조건 트리 (트리와 반대로 홀수 인덱스 짝수 리스트)
    
    ans = []                                        # ans : 트리의 순회 순서를 담은 리스트
    while len(ans) < V :                            # while 조건 : ans에 V를 모두 담을 때까지

        for i in range(1,V+1):                      # for를 통해 1부터 V까지 순회하면서
            if not visit[i] and not required[i]:    # 1) 방문하지 않았고, 2) 선행조건이 남아있지 않은 경우
                ans.append(i)                       # 순회하고 방문 표시
                visit[i] = 1

                for key in tree[i]:                 # 방문한 i에 대해서 트리가 갈 수 있는 곳을 찾고
                    required[key].remove(i)         # 갈 수 있는 곳의 선행조건 i를 삭제한다.
        
    print(f"#{t}", *ans)