t = int(input())

for i in range(t) :
    V,E = map(int,input().split())
    test_dict = dict()
    for j in range(1,V+1):  # 1219와 다르게 V를 기반으로 딕셔너리 미리 다 만들어두기
        test_dict[j] = []

    for _ in range(E):  # 그래프 입력값 받기
        a,b = map(int,input().split())
        test_dict[a].append(b)

    S,G = map(int,input().split())  # 출발지 S 도착지 G
    
    result = 0  # 결과에 대한 변수
    visit = []  # 방문할 곳
    not_visit = []  # 방문해야할 곳

    # 출발지부터 방문해야할 곳에 넣고
    not_visit.append(S)

    while not_visit :
        node = not_visit.pop()  # 노드를 방문해야할 곳 마지막 값을 받음

        if node not in visit :  # 그 노드를 방문하지 않았다면
            visit.append(node)  # 방문한 곳에 넣고
        
        not_visit.extend(test_dict[node])   # 방문하지 않은 곳에 그 노드가 가진 길을 추가적으로 담음

    if G in visit :     # 도착지가 방문한 경로에 담겼다면
        result = 1  # 성공한 것
    print(f"#{i+1} {result}")