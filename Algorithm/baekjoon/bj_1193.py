a = int(input())

n = 0
while True :
    if a > n*(n+1)/ 2 :
        n += 1
    else :
        break

total = n+1 
upper = int(a - (n * (n-1) / 2))
lower = int(total-upper)
if n % 2 == 0 :
    print(f'{upper}/{lower}')
else :
    print(f'{lower}/{upper}')