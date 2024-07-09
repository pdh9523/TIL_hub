x1, y1, z1, x2, y2, z2 = map(int, input().split())
dist = ((x1 - x2)**2 + (y1-y2)**2 + (z1 - z2)**2)**0.5

input()
stick = sorted([*map(int,input().split())])

check=0
if sum(stick) >= dist:
    if stick.pop() - sum(stick) <= dist: check=1
print("YES" if check else "NO")