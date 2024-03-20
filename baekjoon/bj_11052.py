N = int(input())

cards = [0] + list(map(int,input().split()))        # 카드 리스트

DP = [0] * (N+1)

for i in range(1,N+1):
    for j in range(1,i+1):
        # i의 최대값은 그 이하의 카드를 뽑았을 때 최대값 + 카드 값
        DP[i] = max(DP[i], DP[i-j]+cards[j])

print(DP[N])