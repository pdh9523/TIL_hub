N,M = map(int,input().split())

leaf,last=0,0
if M == 2: leaf=1

for i in range(1,N):
    if M>leaf:
        print(0,i)
        leaf+=1
    else : print(last,i)
    last=i