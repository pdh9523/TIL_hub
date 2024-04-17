N,K = map(int,input().split())

table = [False] * 2 + [True] * (N-1)

cnt = 0 
for i in range(2,N+1) :
    if table[i] :
        tmp = 0
        while tmp + i <= N :
            tmp += i
            if table[tmp] :
                table[tmp] = False
                cnt += 1
            if cnt == K :
                exit(print(tmp))