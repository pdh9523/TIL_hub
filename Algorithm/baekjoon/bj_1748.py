def multiple (n) :
    output = 0 
    for i in str(n) :
        output += int(i)
    return output

a = int(input())

count = 0
while a >= 10 :
    a = multiple(a)
    count += 1
print(count)
if a % 3 == 0 :
    print("YES")
else :
    print("NO")