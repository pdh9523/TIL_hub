size = int(input()) # 전체 사람 수

a,b = map(int,input().split())

i = int(input())
test_dict={}
for _ in range(i) :
    test_list = list(map(int,input().split()))
    if test_list[0] in test_dict :
        test_dict[test_list[0]].append(test_list[1])
    else :
        test_dict[test_list[0]] = [test_list[1]]
    for i in range(1,size+1) :
        if i not in test_dict :
            test_dict[i] = []
start = 0
need_visited = []
visited = []

need_visited.append(start)

while need_visited :
    node = need_visited.pop()

    if node not in visited :
        visited.append(node)

        need_visited.extend(test_dict[node])
print(visited)