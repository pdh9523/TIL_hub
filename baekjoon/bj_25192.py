import sys

gomgom = set()
ans = 0 

t = int(input())

for _ in range(t):
    name = sys.stdin.readline().strip()

    if name == "ENTER":
        ans += len(gomgom) 
        gomgom = set()
        continue

    gomgom.add(name)

ans += len(gomgom)

print(ans)