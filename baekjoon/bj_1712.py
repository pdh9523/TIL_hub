a,b,c= map(int,input().split())

if c-b < 0 :
    print(-1)
else :
    count = 0
    while a >= (c-b) * count :
        count+=1

    print(count)