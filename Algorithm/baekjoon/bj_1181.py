a = int(input())
test_set = set()
for i in range(a) :
    test_set.add(input())

test_list = list(test_set)
test_list.sort()
test_list.sort(key=lambda x : len(x))
for ele in test_list :
    print(ele)