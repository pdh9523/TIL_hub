for _ in range(10) :
    i,test_case = map(int,input().split())
    
    test_list = list(map(int,input().split()))

    test_dict = {}
    # 짝수가 시작점, 홀수가 도착점
    for element in range(0,len(test_list), 2) :
        # 시작점을 key, 도착점을 [value]로 담은 딕셔너리
        test_dict[test_list[element]] = test_dict.setdefault(test_list[element], []) + [test_list[element+1]]   
    
    # 출발점은 0 
    start = 0
    # 전체를 방문해야 하니, 방문한 곳과 방문해야할 곳을 나눠서, start에서 출발해서 갈 수 있는 모든 길을 탐색
    need_visited = []
    visited = []

    need_visited.append(start)  # 출발점을 방문해야할 곳에 담고

    while need_visited :    # 방문해야할 곳이 더이상 없을 때 까지 
        node = need_visited.pop()   # 그 값을 노드로 사용

        if node not in visited :    # 그 노드를 방문하지 않았다면
            visited.append(node)    # 방문한 곳에 기록

            if node in test_dict :  # 노드가 딕셔너리에 있다면
                need_visited.extend(test_dict[node])    # 노드에서 갈 수 있는 길을 방문해야할 곳에 담음

    if 99 in visited :
        result = 1 
    else :
        result = 0
    print(f"#{i} {result}")