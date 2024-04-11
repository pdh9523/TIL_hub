for idx in range(int(input())):
    size1,size2 = map(lambda x: int(x)-1,input().split())
    arr1 = sorted(list(map(int,input().split())))
    arr2 = list(map(int,input().split()))

    cnt = 0
    for i in arr2:
        s = 0 
        e = size1
        check = 0 # 1오 2왼
        while s<=e :
            m = (s+e)//2

            if i == arr1[m]:    
                cnt += 1
                break

            elif arr1[m] < i :
                s = m+1
                if check == 1:
                    break
                check = 1
                
            elif arr1[m] > i : 
                e = m-1
                if check == 2:
                    break
                check = 2

    print(f"#{idx+1} {cnt}")