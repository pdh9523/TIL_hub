test_list = [list(map(int,input().split())) for _ in range(5)]
count = 0
rotation = 0 
while rotation < 4 :
    target = map(int,input().split())
    for i in target :
        for arr in test_list : 
            for j in range(len(arr)) :
                if arr[j] == i :
                    arr[j] = 0 # 빙고 칠하기
                    count += 1
                    # 여기서부터 칠할때마다 카운트 올리기
    # 카운트 올릴때마다 빙고 검증하기
        

    tilted_list = [char for char in zip(*test_list)]
    sub_count=0
    for i in test_list :
        if sum(i) == 0 :
            sub_count+=1
    for j in tilted_list :
        if sum(j) == 0 :
            sub_count+=1
    eorkr = 0
    dureorkr = 0
    for k in range(5) :
        eorkr += test_list[k][k]
        dureorkr += test_list[k][4-k]
    if eorkr == 0 :
        sub_count += 1
    if dureorkr == 0:
        sub_count += 1
        
    if sub_count >= 3 :
        print(count)
        break
    rotation += 1

