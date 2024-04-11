t = int(input())
for _ in range(t) :
    a,b = map(int,input().split())
    if a > b :
        a ,b = b, a 
    count = a
    while a % count != 0 or b % count != 0 :
        count -=1
    print(int(a*b/count))