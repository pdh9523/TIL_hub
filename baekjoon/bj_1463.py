a = int(input())
count =0
while a > 1 : 
    if a % 3 == 0 :
        a = a/3
        count+=1
        continue
    elif a % 9 == 1 :
        a -= 1
        count+=1 
        continue
    elif a % 2 == 0 :
        a = a/2
        count+= 1
        continue
    else :
        a-=1
        count+=1

print(count)
