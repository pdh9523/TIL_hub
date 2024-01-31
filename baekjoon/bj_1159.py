t = int(input()) 
test_case = {}
for _ in range(t) :
    a = input()
    test_case[a[0]] = test_case.setdefault(a[0], 0) + 1
test_list = []
for key, value in test_case.items() :
    if test_case[key] >= 5  :
        test_list.append(key)

test_list.sort()
if len(test_list) == 0 :
    print("PREDAJA")
else :
    print(*test_list, sep="")
