N = int(input())

DP = [1] * 10

for _ in range(N-1):
    DP2 = [0]*10
    for i in range(10):
        DP2[i] = sum(DP[:i+1])%10007
    DP = DP2[:]
print(sum(DP)%10007)