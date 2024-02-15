t = int(input())
for x in range(t) :
    V,E = map(int,input().split())
    test_dict = {}
    for i in range(E) :
        test_list = list(map(int,input().split()))
        if test_list[0] not in test_dict :
            test_dict[test_list[0]] = [test_list[1]]
        else :
            test_dict[test_list[0]].append(test_list[1])
    S,G = map(int,input().split())
    
    idx = S
    location = 0
    stack = [] 
    result = 1
    while result == 1 :     # 이거 좋네요
        location = min(test_dict[idx])
        test_dict[idx].remove(location)
        stack.append(idx)
        idx = location

        if idx == G :
            break
        
        while idx not in test_dict or test_dict[idx] == [] :
            if len(stack) == 0 :
                result = 0
                break
            else :
                idx = stack.pop()
            
    print(f"#{x+1} {result}")