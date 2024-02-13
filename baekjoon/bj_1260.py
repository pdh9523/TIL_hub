N,M,V = map(int,input().split())
test_list = [[] for _ in range(N+1)]
for _ in range(M) :
    t,c = map(int,input().split())
    test_list[t].append(c)
    test_list[c].append(t)

start = V

visit = []
not_visit = [start]

stack = [start]  # 스택 리스트
idx = V     # 현재 인덱스 (인덱스에서 전처리를 하고 위치를 바꿔야한다.)
location = V    # 현재 위치
visited = []
while stack :
    if location not in visited :
        visited.append(location)
    location = min(test_list[idx])  # 위치를 idx에 담긴 value의 작은 값부터 순회
    stack.append(location)   # 찍었으니 스택에 담고
    test_list[idx].remove(location)  # 한번 찍은 길은 딕셔너리에서 제거
    idx = location  # 이후의 탐색에서 다시 위치를 인덱스로 탐색

    while idx not in test_list or test_list[idx] == [] :    # 더이상 길이 없다
        if len(stack) == 0 :    # 근데 심지어 스택도 다 비었다
            break
        else :  # 스택에 있긴 하다
            idx = stack.pop()   # idx를 직전에 갔던 길로 사용한다.
print(visited)