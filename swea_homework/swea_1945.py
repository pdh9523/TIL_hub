t = int(input())

for i in range(t) :
    test_case = int(input())

    result = [0 for x in range(5)]
    while test_case % 2 == 0 :
        test_case /= 2
        result[0] += 1
    while test_case % 3 == 0 :
        test_case /= 3
        result[1] += 1
    while test_case % 5 == 0 :
        test_case /= 5
        result[2] += 1
    while test_case % 7 == 0 :
        test_case /= 7
        result[3] += 1
    while test_case % 11 == 0 :
        test_case /= 11
        result[4] += 1
    print(f"#{i+1}", *result)
    