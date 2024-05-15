for _ in range(int(input())):
    N = int(input())
    arr2 = [*map(int,input().split())]
    dic = dict()

    M = int(input())
    arr1 = [*map(int,input().split())]

    for i in arr1 : 
        dic[i] = 0

    for j in arr2 :
        if dic.get(j)==0:
            dic[j]+=1

    for i in arr1:
        print(dic[i])