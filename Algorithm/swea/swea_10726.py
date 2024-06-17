for tc in range(int(input())):
    N,M = map(int,input().split())

    for i in range(N):
        if (1<<i & M):
            ans = "ON"
        else :
            ans = "OFF"
            break
    print(f"#{tc+1} {ans}")