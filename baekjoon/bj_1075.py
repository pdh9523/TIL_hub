a = int(input()[:-2] + '00')
b = int(input())

output = 0
while a % b > 0 :
    a +=1
    output += 1

print(("{:02d}").format(output))