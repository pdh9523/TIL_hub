while True :
    N = int(input())
    if not N :
        break

    table = [1] * (2*N+1)
    
    table[0] = table[1] = 0
    
    for i in range(2, 2*N+1):
        if table[i]:
            tmp = i
            while tmp+i < 2*N+1 :
                tmp += i 
                table[tmp] = 0
    print(sum(table[N+1:]))