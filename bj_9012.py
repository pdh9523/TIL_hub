a = int(input())

for i in range(a) :
    test_case = input()
    output = 0
    if test_case[0] == ")" :
        print("NO")
    else :
        for j in test_case :
            if j == "(" :
                output += 1
            if j == ")" :
                output -= 1 
            if output < 0 :
                print("NO")
                break
        
        if output == 0 :
            print("YES")
        elif output > 0 :
            print("NO")