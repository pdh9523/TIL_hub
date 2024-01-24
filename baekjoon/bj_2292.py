# 0 - 6 - 18 - 36 - 60
a = int(input())

target = (a-1) / 6

if (a-1) % 6 == 0 :
    target-= 0.1
# 0 - 1 - 1+2 - 1+2+3 - 1+2+3+4 - 1+2+3+4+5
# 19, 37 이렇게 나눠 떨어질 떄 문제 발생 
n = 1
while target >= (n+1)*n / 2 :
    if a == 1 :
        break
    n += 1

if a == 1 :
    print(1)
else :
    print(n+1)