def calculate(n):
    return cows[(n-3)%N]*cows[(n-2)%N]*cows[(n-1)%N]*cows[n%N]


N,Q = map(int,input().split())
cows = [*map(int,input().split())]
alts = [*map(lambda x : int(x)-1,input().split())]

data = [calculate(n) for n in range(N)]

# for alt in alts:
#     cows[alt-1] *= -1
#     print(sum([calculate(n) for n in range(N)]))
# 무조건 시간 초과 날테니 시도 조차 안함 (방향성 맞는지만 검증)

ans = sum(data)
for alt in alts:
    for i in range(4):
        data[(alt+i)%N] *= -1
        # 여기서, -1만 곱하면 돼서 굳이 이럴 필요가 없긴함
        ans += 2*(data[(alt+i)%N])
    print(ans)

# 1 2 3 4
# 2 3 4 5
# 3 4 5 6
# 4 5 6 7
# n-3 n-2 n-1 n
# 10 11 12 1
# 11 12 1 2
# 12 1 2 3
# 1 2 3 4

# 1을 고치려면 4개를 바꿔야함