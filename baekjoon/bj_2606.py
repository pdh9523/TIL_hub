a = int(input())
b = int(input())
temp_list = []
for i in range(b):
    temp_set = set(map(int, input().split()))
    temp_list.append(temp_set)

for j in range(len(temp_list)):
    for k in range(len(temp_list)):
        if temp_list[j] & temp_list[k]:
            temp_list[j].update(temp_list[k])

output = 0
for k in temp_list:
    if 1 in k:
        rem = len(k)
        if rem > output:
            output = rem

if output == 0:
    print(0)
else:
    print(output-1)
