import sys
sys.stdin = open("1219.txt")

for _ in range(10) :
    t, test_case = map(int,input().split())

    test_list = list(map(int,input().split()))
    test_dict = {}
    for idx in range(0,len(test_list),2) :
        if test_list[idx] not in test_dict :
            test_dict[test_list[idx]] = [test_list[idx+1]]
        else :
            test_dict[test_list[idx]].append(test_list[idx+1])
        
    result=0

    idx = 0
    stack = []
    location = 0
    count = 1

    while True :
        location = min(test_dict[idx])
        stack.append(min(test_dict[idx]))
        test_dict[idx].remove(min(test_dict[idx]))
        idx = location

        if idx == 99 :
            result = 1
            break
        while (idx not in test_dict) or test_dict[idx] == [] :
            if len(stack) > 0 :
                idx = stack.pop()
            else :
                break

    print(f"#{t} {result}")