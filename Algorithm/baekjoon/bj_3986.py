import sys
input = sys.stdin.readline

ans = 0
for _ in range(int(input())):
    s = []
    for char in input().strip():
        if s and s[-1] == char: s.pop()
        else: s.append(char)
    if not s: ans +=1
print(ans)