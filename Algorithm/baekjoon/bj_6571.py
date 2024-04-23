while True:
    arr = [0,1,2]
    N,M = map(int,input().split())
    if (N,M) == (0,0) :
        break

    cnt = 0

    if N < 2 :
        if M < 3 :
            cnt += M
        else :
            cnt += 2

    elif N == 2: 
        cnt += 1

    while True:
        temp = arr[-1] + arr[-2]
        if temp <= M :
            arr.append(temp)
            if N <= temp <= M :
                print(temp)
                cnt += 1
        else :
            break

    print(cnt)