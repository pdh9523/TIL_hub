a = input()
target = int(a)

if (target%10) + (target//10) >= 10 :
    target = (target%10) * 11 + (target//10) - 10
else :
    target = (target%10) * 11 + (target//10)
rem = 1 # 횟수

while a != str(target) :
    rem += 1
    if (target%10) + (target//10) >= 10 :
        target = (target%10) * 11 + (target//10) - 10
    else :
        target = (target%10) * 11 + (target//10)
    
print(rem)