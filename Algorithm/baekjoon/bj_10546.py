import sys; input = sys.stdin.readline


N = int(input())
data = set()
for _ in range(2*N-1):
    a = input()
    if a in data: data.remove(a)
    else: data.add(a)
print(*data)
