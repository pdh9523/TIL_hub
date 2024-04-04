import sys

input = sys.stdin.readline

N = int(input())

company = dict()

for _ in range(N):
    a = input().split()
    if a[1] == 'enter':
        company[a[0]] = 1
    else :
        company.pop(a[0])
print(*sorted(company.keys(), reverse=True), sep="\n")