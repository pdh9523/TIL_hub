import sys

input = sys.stdin.readline

N,M = map(int,input().split())

strings = dict()

for _ in range(N):
    strings[input().strip()] = 1

cnt = 0 
for _ in range(M):
    target = input().strip()
    if strings.get(target) :
        cnt += 1

print(cnt)