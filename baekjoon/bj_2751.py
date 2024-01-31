a = int(input())
rem = []
for _ in range(a) :
    rem.append(int(input()))

rem.sort()
print(*rem, sep="\n")