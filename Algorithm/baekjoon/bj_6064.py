T = int(input())

for _ in range(T):

    M, N, x, y = map(int, input().split())

    check = True
    while x <= M * N and check:
        if (x-y) % N == 0 :
            ans = x
            check = False
        x += M
    
    if not check:
        print(ans)
    else :
        print(-1)