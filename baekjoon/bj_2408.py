a= int(input())
output = ""
for _ in range(2*a - 1) :
    output += input()

result = int(eval(output))

if result < 0 :
    print(result-1)

else :
    print(result)