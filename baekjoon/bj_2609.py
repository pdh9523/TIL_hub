a,b = map(int,input().split())

if b > a :
    a, b = b, a 

div = a

for i in range(a) :
    if a % div == 0 and b % div == 0 :
        break
    else :
        div -= 1

print(div)
print(int(a*b/div))