import sys
input = sys.stdin.readline

N,M = map(int,input().split())

stat = [set() for _ in range(N)]
men = []
for _ in range(N):
    data = [*map(int,input().split())]
    for i in range(3):
        stat[i].add(data[i])
    men.append(data)
ans = float('inf')

for i in sorted(stat[0]):
    for j in sorted(stat[1]):
        for k in sorted(stat[2]):
            if i+j+k >= ans:
                break
            tmp = 0
            for a,b,c in men:
                if i>=a and j>=b and k>=c:
                    tmp += 1

            if tmp >=M:
                ans = min(ans, i+j+k)
print(ans)