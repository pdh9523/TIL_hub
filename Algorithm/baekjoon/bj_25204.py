import sys
input = sys.stdin.readline

def check(x):
    res = ""
    for char in x:
        res += char
        if char.isupper():
            res = res[:-1]+chr(ord(char)-1)
        elif char == "-":
            res = res[:-1]+"{"

    return res.lower(),res

for _ in range(int(input())):
    arr = sorted([input().strip() for _ in range(int(input()))], key=check)
    print(*arr, sep="\n")