idx = int(input())

for i in range(idx) :
    t = int(input())

    empty_list = [[0 for _ in range(t)] for _ in range(t)] # 일단 0으로 채운 t*t 2차원 빈 리스트 생성
    numbers = list(range(1,t**2+1)) # 위 리스트에 들어갈 일차원 숫자 리스트 생성

    # 초기값 설정
    x, y, count,d_count = 0, 0, 0, 0

    # 0,0 0,1 0,2 1,2 2,2 2,1 2,0 1,0 1,1 순서.
    empty_list[x][y] = numbers[count] # 첫 배열 색칠
    
    while count < t**2-1 : # 종료 조건 : list를 다 덮는 경우 (칠할때마다 카운트가 올라가고, 카운트 -1 이면 다 덮힘)
        # 총 4개의 경우 (x,y가 0 또는 t-1에 닿는 경우)
        while y < t-1 : 
            y+=1 # 닿을때까지 전진하고
            if empty_list[x][y] != 0: # 0이 아니다 (다른 숫자가 들어가있다)
                y-=1 # 위에서 올렸던거 하나 내리고 
                break # 다음 경우의 수로 넘어감
            count+=1
            empty_list[x][y] = numbers[count]

        while x < t-1 :
            x+=1     
            if empty_list[x][y] != 0:
                x-=1
                break
            count+=1
            empty_list[x][y] = numbers[count]
        while y > 0 :
            y -= 1
            if empty_list[x][y] != 0:
                y+=1
                break
            count+=1
            empty_list[x][y] = numbers[count]
        while x > 0 :
            x -= 1
            if empty_list[x][y] != 0:
                x+=1
                break
            count+=1
            empty_list[x][y] = numbers[count]

    print(f"#{i+1}")
    for arr in empty_list :
        print(*arr)