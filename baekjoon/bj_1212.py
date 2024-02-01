a = list(input())
output = ""
for i in a :
    output+=("{:0b}".format(int(i))).zfill(3)

print(output.lstrip("0"))