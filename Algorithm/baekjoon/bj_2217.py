t = int(input())
test_list = []
for _ in range(t) :
    test_list.append(int(input()))

test_list.sort()
t
for idx in range(t) :
    test_list[idx] = test_list[idx]*(t-idx)

print(max(test_list))