test = int(input())

for i in range(test) :
    p,q,r,s,w = map(int,input().split())
    a_value = 0
    b_value = 0
    output=0
    a_value = w*p
    if w>r :
        b_value = q + ((w-r)*s)
    if w<=r :
        b_value=q

    if a_value > b_value :
        output=b_value
    else : 
        output=a_value
    print("#{} {}".format((i+1),output))