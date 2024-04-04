password = [
    [7],[2,4],[1,3,5],[2,6],[1,5,7],[2,4,6,8],[3,5,9],[4,8,0],[5,7,9],[6,8]
]


T = int(input())

for _ in range(T) :
    N = int(input())
    DP = [1]*10
    for i in range(1,N) :
        DP2 = [0]*10
        for j in range(10) :
            for k in password[j] :
                DP2[j] = (DP2[j] + DP[k]) % 1234567
        
        DP=DP2[:]

    print(sum(DP)%1234567)