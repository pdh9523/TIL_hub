import sys; input = sys.stdin.readline


kang = {"ChongChong"}
for _ in range(int(input())):
    chong = set(input().split())
    if kang & chong:
        kang.update(chong)
print(len(kang))