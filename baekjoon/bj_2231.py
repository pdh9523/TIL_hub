a = input()
ans = int(a)
result = []
while a :
    a= str(a)
    b = sum(map(int,list(a))) + int(a)
    if b == ans:
        result.append(int(a))
    a = int(a)-1
if result :
    print(min(result))
else :
    print(0)