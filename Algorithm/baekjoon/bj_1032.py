a = int(input())
arr = []
for i in range(a) :
    b = input()
    arr.append(b)

output = ""

for j in range(len(b)) :
    temp_set = set()
    for k in range(a) :
        temp_set.add(arr[k][j])
    if len(temp_set) == 1 :
        output += arr[0][j]
    else :
        output += "?"
print(output)