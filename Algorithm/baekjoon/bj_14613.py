W,L,D = map(float,input().split())

DP = [[0]*3001 for _ in range(21)]
DP[0][2000] = 1

for i in range(1,21):
    for j in range(1000,3001):
        if DP[i-1][j] == 0 :
            continue
        # 승
        if j+50 <= 3000:
            DP[i][j+50] += DP[i-1][j] * W
        # 패
        if j-50 >= 1000:
            DP[i][j-50] += DP[i-1][j] * L
        # 무
        DP[i][j] += DP[i-1][j] * D

b,s,g,p,d=0,0,0,0,0

for i in range(3001):
    if 1000 <= i < 1500:
        b += DP[20][i]
    elif 1500 <= i < 2000:
        s += DP[20][i]
    elif 2000 <= i < 2500:
        g += DP[20][i]
    elif 2500 <= i < 3000:
        p += DP[20][i]
    elif 3000 <= i < 3500:
        d += DP[20][i]

for i in b,s,g,p,d:
    print(f"{i:.8f}")


