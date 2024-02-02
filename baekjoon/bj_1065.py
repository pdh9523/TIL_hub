a = int(input()) # 밑에 str로 쓸건데 왜 int로 받나요 ? 떼서 쓰려구요
count=0
for i in range(1,a+1) : # 여기서도 int로 써야되구요
    test_case = list(map(int,str(i))) # 각 자리수를 리스트로 매핑

    if a < 10 : # a가 10 미만이면 무조건 등차수열을 이룹니다. 혼자니까요
        count += 1
    
    else :
        dif_set = set() # 빈 세트 지정
        for idx in range(1,len(test_case)) : # 각 자리수가 담긴 리스트의 각 인덱스에서
            char=test_case[idx]-test_case[idx-1] # 자리수를 빼서
            dif_set.add(char) # 세트에 add 합니다.
        if len(dif_set) <= 1 : # 세트가 1개 이하다 (등차거나 차이가 없다)
            count+=1 # 카운트 올립니다.
print(count)