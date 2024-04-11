a = int(input())    # 테케 개수

for i in range(a) :

    test_case = input()    # 테케
    output = 0

    if test_case[0] == ")" :    # 처음부터 )이면 NO
        print("NO")

    else :  
        for j in test_case :    
            if j == "(" :       # 괄호를 여는 것을 +1, 닫는 것을 -1로 두면 마지막에 0 이 되어야 하고
                output += 1

            if j == ")" :   
                output -= 1 

            if output < 0 :     #  음수로 떨어지면 잘못된 것
                print("NO")
                break
        
        if output == 0 :    # 순회를 마친 후 output이 0 이어야 정상
            print("YES")

        elif output > 0 :   # output이 남아 있으면 잘못된 것
            print("NO")