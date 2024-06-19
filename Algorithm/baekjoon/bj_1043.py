# N 사람 수, M 파티 수 
N,M=map(int,input().split())

# truth : 진실을 아는 사람
truth = set(input().split()[1:])

# members : 파티의 사람 
members = [set(input().split()[1:]) for _ in range(M)]

# 모든 파티의 사람들을 다 합친 다음,
for _ in range(M):
    for member in members:
        if member&truth: truth |= member

# 진실을 아는, 알게되는 애들이랑만 얘기 안하면 된다.
cnt = 0
for member in members:
    if not member&truth : cnt += 1
print(cnt)