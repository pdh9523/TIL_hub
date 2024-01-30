a = int(input())
count=0
for i in range(1,a+1) :
    test_case = list(map(int,str(i)))
    dif_set = set()
    if a < 10 :
        count += 1
    else :
        for idx in range(1,len(test_case)) :
            char=test_case[idx]-test_case[idx-1]
            dif_set.add(char)
        if len(dif_set) <= 1 :
            count+=1
print(count)