a = int(input())
div = 2
while a > 1 :
    if a % div == 0 :
        a = a//div
        print(div)
    else : 
        div+=1