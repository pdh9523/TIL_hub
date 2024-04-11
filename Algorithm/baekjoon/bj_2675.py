rot = int(input())

for i in range(rot) :
    test_case = input().split()
    multiple = int(test_case[0])
    case = test_case[1]
    for j in case : 
        print(j*multiple, end="")
    print()