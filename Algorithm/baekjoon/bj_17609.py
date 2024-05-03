import sys

input = sys.stdin.readline


def check(left, right, chk=0):

    while left < right :
        if text[left] != text[right] and chk == 0:
            a = check(left+1, right, chk+1)
            b = check(left, right-1, chk+1)
            return min(a,b)

        elif text[left] != text[right] and chk == 1:
            return 2

        else :
            left+=1
            right-=1
    return chk

for _ in range(int(input())):
    text = input().strip()
    print(check(0,len(text)-1))