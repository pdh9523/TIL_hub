for tc in range(1,int(input())+1):

    N,M = map(int,input().split())
    arr = {k:True for k in input().split()}
    brr = {k:True for k in input().split()}
    cnt = 0
    for i in arr:
        if i in brr: cnt += 1
    
    print(f"#{tc} {cnt}")