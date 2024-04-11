for idx in range(10) :
    count = int(input())
    a = list(map(int,input().split()))
    a.sort() # 정렬하고

    while count > 0 : # 카운트가 다 떨어질때까지 +1 / -1 / 정렬을 반복
        a[0] += 1 # 최소값은 1 올리고
        a[-1] -= 1 # 최대값은 1 내리고
        a.sort() # 다시 정렬
        count -= 1 # 카운트 1 내림
    print(f"#{idx+1} {max(a)-min(a)}") # 결과를 반환 