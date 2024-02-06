import sys
a = int(sys.stdin.readline())
test_dict = {}
for i in range(a) :
    test_case = int(sys.stdin.readline())
    if test_case not in test_dict : 
        test_dict[test_case] = 1
    else :
        test_dict[test_case] += 1

for j in range(max(test_dict)+1) :
    if j in test_dict :
        for k in range(test_dict[j]) :
            print(j)