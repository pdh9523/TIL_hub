for idx in range(int(input())):
    N = int(input())
    arr = list(map(int,input().split()))

    under = sorted(arr[:N//2])

    upper = sorted(arr[N//2:N])

    print(under, upper)