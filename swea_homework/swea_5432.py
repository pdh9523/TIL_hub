t = int(input())
for i in range(t) :
    test_case = input()

    count = 0
    result = 0
    idx = 0
    while idx < len(test_case) :
        if test_case[idx] == "(" :
            count += 1
            result += 1
            if test_case[idx+1] == ")" :
                count -=1 
                result+= count -1
                idx+=1
        elif test_case[idx] == ")" :
            count -= 1 

            
        idx += 1

    print(f"#{i+1} {result}")