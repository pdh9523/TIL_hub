a =int(input())

test_case = list(input())
output = 0
for i in test_case : 
    if i == "L" :
        output += 0.5
    if i == "S" :
        output += 1

if output != a :
    output += 1

print(int(output))