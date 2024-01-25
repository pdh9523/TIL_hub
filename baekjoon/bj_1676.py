b = int(input())
a = list(range(1,b+1))
count = 0
if b == 0 :
    pass
else :
    while max(a) > 0 :
        for i in range(len(a)) :
            if a[i] % 5 == 0 :
                a[i] = a[i]/5
            else : 
                a[i] = 0
        count += len(a) - a.count(0) 
print(count)