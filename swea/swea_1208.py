for idx in range(10) :
    count = int(input())
    a = list(map(int,input().split()))
    a.sort()

    while count > 0 :
        a[0] += 1
        a[-1] -= 1
        a.sort()
        count -= 1
    print(f"#{idx+1} {max(a)-min(a)}")