a=int(input())

for i in range(a) :
    b,c = map(int,input().split())
    print ("#{} {} {}".format((i+1), (b//c), (b%c)))