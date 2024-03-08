N = int(input())

length = list(map(int,input().split()))
gas = list(map(int,input().split()))
gas.pop()
# 첫번째 집에서 충전해야함
# 각 도시에서 가격을 비교하면서
# 이후의 도시가 가격이 더 싸면
# 거기까지 갈 수 있는 기름 풀충전

