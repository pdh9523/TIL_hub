import sys; input = sys.stdin.readline

S,N,M = map(int,input().split())

cnt = 0
for _ in range(N+M):
    a = int(input())
    if a:
        cnt += 1
        if cnt > S:
            S *= 2
    else:
        cnt -= 1

print(S)