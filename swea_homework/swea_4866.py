t = int(input())

for i in range(t) :

    test_case = input()

    test_list = []
    in_list = ["(", "{"]
    out_list = [")", "}"]
    result = 1
    for char in test_case :
        if char in in_list :
            test_list.append(char)
        if char == "}" :
            if len(test_list) == 0 or test_list[-1] == "(" :
                result = 0
                break
            else :
                test_list.pop()
        if char == ")" :
            if len(test_list) == 0 or test_list[-1] == "{" :
                result = 0
                break
            else :
                test_list.pop()
    if len(test_list) >0 :
        result=0
    print(f"#{i+1} {result}")