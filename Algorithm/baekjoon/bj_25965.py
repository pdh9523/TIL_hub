for _ in range(int(input())):
    ans = 0
    missions = []
    for _ in range(int(input())):
        missions.append([*map(int,input().split())])
    K,D,A = map(int,input().split())
    for mission in missions:
        k,d,a = mission
        tmp = k*K - d*D + a*A
        if tmp>0:
            ans += tmp

    print(ans)