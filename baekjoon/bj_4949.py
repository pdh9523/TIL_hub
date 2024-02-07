a = input()
open_list=["[","("]
while a != "." :
    test_list=[]
    for char in a :
        if char in open_list :
            test_list.append(char)
        elif char == "]" :
            if len(test_list) == 0 or test_list[-1] != "[" :
                print("no")
                break
            else :
                test_list.pop()

        elif char == ")" :
            if len(test_list) == 0 or test_list[-1] != "(" :
                print("no")
                break
            else :
                test_list.pop()
    else :
        if len(test_list) == 0 :
            print("yes")
        else :
            print("no")

    a=input()
    test_list=[]
