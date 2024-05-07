import sys

input = sys.stdin.readline


tmp = dict()
for _ in range(int(input())):
    a,b = input().strip().split(".")

    tmp[b] = tmp.get(b,0)+1

for i in sorted(tmp.keys()):
    print(i, tmp[i])