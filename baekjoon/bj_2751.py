import sys
a = int(input())
rem = []
for _ in range(a) :
    rem.append(int(sys.stdin.readline()))

rem.sort()
print(*rem, sep="\n")