a = int(input())
for i in range(a) :
    h,w,n = map(int,input().split())
    if n % h == 0 :
        floor = h
        hosu = n//h
    else : 
        floor = n%h
        hosu = (n//h) +1
    print(str(floor)+str(hosu).zfill(2))