for idx in range(10):
    a = int(input())
    test_list = list(map(int,input().split()))
    output = 0 
    for i in range(2,len(test_list)-2) :
        if max(test_list[i-2:i+3]) == test_list[i] :
            max_list = test_list[i-2:i+3]
            max_list. remove(test_list[i])
            plus = test_list[i] - max(max_list)
            output += plus
    print(f"#{idx+1} {output}")