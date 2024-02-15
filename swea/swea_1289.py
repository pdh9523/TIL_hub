t =int(input())

for i in range(t) :
    test_case = input()
    bit = '0'
    count = 0
    for idx in range(len(test_case)) :
        if test_case[idx] != bit :
            count +=1
            bit=test_case[idx]
    print(count)