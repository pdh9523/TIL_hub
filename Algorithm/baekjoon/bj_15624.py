a,b = 0,1
for _ in range(int(input())):
    c = (a+b) % 10**9+7
    a,b = b,c
print(a)