import math

a = int(input())
test_list = []

for i in range(a) :
    test_list.append((int(input())))

test_list.sort()

test_dict = {}

for element in test_list :
    if element not in test_dict :
        test_dict[element] = 1
    else :
        test_dict[element] += 1
rem = 0
result = 0

for key,value in test_dict.items() :
    if value >= rem :
        rem = value
        result = key

key_list = []

for key, value in test_dict.items() :
    if value == rem :
        key_list.append(key)

key_list.sort()


print(round((sum(test_list)/a))) #산술평균
print(test_list[(a//2)])
if len(key_list) == 1:
    print(key_list[0])
else :
    print(key_list[1])
print(max(test_list)-min(test_list))
