num = input()

a = sum([int(i) for i in num])
c = int(a>=10)

while a >= 10:
    a = sum([int(i) for i in str(a)])
    c += 1
print(c)
print(["YES","NO"][a%3!=0])