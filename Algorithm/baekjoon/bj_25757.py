import sys; input = sys.stdin.readline

data = {
    "Y": 1,
    "F": 2,
    "O": 3,
}

N,M = input().split()
men = set()
for _ in range(int(N)):
    men.add(input().strip())

print(len(men)//data[M])