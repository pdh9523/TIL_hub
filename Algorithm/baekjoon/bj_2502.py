# 첫째날 n , 둘째날 m

# X 번쨰 날 : n, m, (n+m), n+2m, 2n+3m, 3n+5m, 5n+8m, 8n+13m,
# 3 일째부터   n : 1 1 2 3 5 8 13
# 3 일째부터   m : 1 2 3 5 8 13 21 


N,K = map(int,input().split())

N-=3 

fibo = [1,1]

for _ in range(N):
    fibo.append(fibo[-1]+fibo[-2])

for A in range(1,K-1):
    for B in range(A+1,K):
        if fibo[-2] * A + fibo[-1] * B == K:
            exit(print(A,B, sep="\n"))
            
        elif fibo[-2] * A + fibo[-1] * B > K:
            continue