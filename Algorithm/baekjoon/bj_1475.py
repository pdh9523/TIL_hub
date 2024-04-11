import math
a = list(map(int,list(input())))
test_dict = {}

for j in range(10) :
    test_dict[j] = 0
for i in a : 
    test_dict[i] += 1
test_dict[69] = math.ceil((test_dict[6]+test_dict[9]) / 2)
del test_dict[6]
del test_dict[9]

print(max(test_dict.values()))