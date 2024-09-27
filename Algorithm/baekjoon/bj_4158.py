while True:
    N,M = map(int,input().split())
    if N==0 and M==0: break
    arr = set(int(input()) for _ in range(N))
    brr = set(int(input()) for _ in range(M))

    print(len(arr&brr))