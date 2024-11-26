for _ in range(int(input())):

    A,B,C = map(int,input().split())
    AB,BC,CA = map(int,input().split())

    ans = -float('inf')
    for ab in range(min(A,B)+1):
        if BC>CA:
            bc = min(B-ab,C)
            res = AB*ab + BC*bc + CA*(min(C-bc, A-ab))

        else:
            ca = min(C,A-ab)
            res = AB*ab + CA*ca + BC*(min(B-ab, C-ca))

        ans = max(ans,res)
    
    print(ans)