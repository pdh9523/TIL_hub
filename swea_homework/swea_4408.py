import math 

t = int(input())

for i in range(t) :
    test_list = [0] * 201
    N = int(input())
    for _ in range(N) :
        a,b = map(int,input().split())
        if a > b :
            a,b = b,a
        a = math.ceil(a // 2)
        b = math.ceil(b // 2)

        for idx in range(a,b+1) :
            test_list[idx] += 1
    print(f"#{i+1} {max(test_list)}")