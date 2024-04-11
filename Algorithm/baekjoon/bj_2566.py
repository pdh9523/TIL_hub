test_list = []
for i in range(9) :
    inner_list=[]
    a = list(map(int,input().split()))
    rem = 0
    rem_index = 0
    for j in range(len(a)) :
         if a[j] > rem :
            rem,rem_index = a[j], j
    inner_list.append(rem)
    inner_list.append(i+1)
    inner_list.append(rem_index+1)
    test_list.append(inner_list)

rem_2 = 0
rem_index_2 = 0 
for k in range(len(test_list)) :
    if rem_2 < test_list[k][0] :
        rem_2 = test_list[k][0]
        rem_index_2 = k
print(rem_2)
print(test_list[rem_index_2][1], test_list[rem_index_2][2])
