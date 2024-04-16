for _ in range(int(input())):

    N = int(input())
    div = dict()

    for i in range(2,N+1):

        while N % i == 0 :
            N //= i
            div[i] = div.get(i,0)+1
        
        if i == 1 :
            break
    for ans in div.items():
        print(*ans)