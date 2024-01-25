a = int(input())
b = list(map(int,input().split()))

c = int(input())
d = list(map(int,input().split()))

test_list = []
for i in d :
    test_list.append(b.count(i))
print(*test_list)