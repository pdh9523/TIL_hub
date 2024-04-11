a = int(input())

count = 0

if a == 1 or a == 3 :
    print(-1)
else :
    while a > 0 :
        if a % 2 != 0 :
            a -= 5
            count += 1
        elif a >= 10 and a % 2 == 0 :
            a -= 10
            count += 2
        else :
            a -= 2
            count += 1
    print(count)