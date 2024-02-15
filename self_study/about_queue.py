from collections import deque


for _ in range(10) :

    t = int(input())

    a = deque()
    a.extend(map(int,input().split()))

    while a[-1] != 0 :
        for i in range(1,6) :
            code = a.popleft()-i
            if code <= 0 :
                code = 0
            a.append(code)
            
    print(f"#{t}",*a)