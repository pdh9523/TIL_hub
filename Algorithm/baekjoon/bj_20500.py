# 15 : 3의 배수이면서 5의 배수
# 5의 배수 : 끝자리가 5 또는 0 
# 3의 배수 : 각 자리 수 합이 3
# 숫자가 1또는 5로 구성되기 때문에 뒷자리는 무조건 5다.

# 뒤에 5를 계속 붙이면서 값을 비교하면 되지 않나
N = int(input())

DP = [[0,0,0] for _ in range(N+1)] # 나머지가 0일때, 나머지가 5일때, 나머지가 10일때

DP[1][1] = 1
d = 1000000007
# 뒤의 5를 고정하고 앞으로 하나씩 붙이면서 값을 만들면서 점화식을 구성
for i in range(2,N+1):
    DP[i][0] = (DP[i-1][1]+DP[i-1][2]) % d
    DP[i][1] = (DP[i-1][0]+DP[i-1][2]) % d
    DP[i][2] = (DP[i-1][0]+DP[i-1][1]) % d

print(DP[N][0] % d)