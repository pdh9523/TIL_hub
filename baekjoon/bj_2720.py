test_case = int(input())

for test in range(test_case) :
    count = []
    test = int(input())
# 25
    if test >= 25 :
        count.append(test//25)
        test = test % 25
    elif test // 25 == 0 :
        count.append(0)
# 10        
    if test >= 10 :
        count.append(test//10)
        test = test % 10
    elif test // 10 == 0 :
        count.append(0)
# 5
    if test >= 5 :
        count.append(test//5)
        test = test % 5
    elif test // 5 == 0 :
        count.append(0)
# 1        
    count.append(test)
    for j in count :
        print(j, end=" ")
    if test != test_case-1 :
        print()