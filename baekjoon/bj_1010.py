def fac(n) :
    if n == 0 :
        return 1
    else :
        return n * fac(n-1)


test_case = int(input())


for i in range(test_case) :
    n,m= map(int,input().split())
    print(fac(m) // (fac(m-n) * fac(n)))        # 다리는 mCn