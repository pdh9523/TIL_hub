a = int(input())
temp_dict = {}
for _ in range(a) :
    b = input()
    temp_dict[b] = temp_dict.setdefault(b, 0) + 1
rem = 0
result = ""
keys = list(temp_dict.keys())
keys.sort()

rem = 0
result = "" 
for key in keys :
    if temp_dict[key] > rem :
            rem = temp_dict[key]
            result = key
print(result)