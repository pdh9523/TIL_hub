a = int(input())

for i in range(a) :
    count = 0
    result = 0
    test_case = input()
    for j in test_case : 
        if j == "O" :
            count +=1
            result += count
        else : 
            count = 0 
    print(result)