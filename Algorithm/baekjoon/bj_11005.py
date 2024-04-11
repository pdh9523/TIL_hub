a,b = map(int,input().split())
output = ""
while a > 0 :
    c = a%b
    if c > 9 :
        c = chr(55+c) #65가 A
    output += str(c)
    a = a // b
print(output[::-1])