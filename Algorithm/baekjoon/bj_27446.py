N,M = map(int,input().split())
DP = [0] * (N+2)
arr = sorted(set(range(1,N+1)) - set(map(int,input().split())))

for char in arr :
    if char == 1 or not(DP[char-1] or DP[char-2] or DP[char-3]) :
        DP[char] = 7
        if DP[char-2] :
            DP[char-1] = 2
        if DP[char-3] :
            DP[char-2] = DP[char-1] = 2
    else :
        if DP[char-2] :
            DP[char-1] = 2
        if DP[char-3] :
            DP[char-2] = DP[char-1] = 2
        DP[char] = 2
print(sum(DP))