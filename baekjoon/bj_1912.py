t = int(input())

arr = list(map(int,input().split()))

DP = [0] * t
DP[0] = arr[0]
for i in range(1,t):
    if DP[i-1] < 0 :
        DP[i] = arr[i]
    else :
        DP[i] = DP[i-1] + arr[i]
print(max(DP))
