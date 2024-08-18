from math import ceil

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [*map(int, input().split())]

    while N > 2:
        tmp = []
        for i in range(ceil(N/2)):
            tmp.append(arr[i] + arr[-i-1])
        arr = tmp[:]
        N = ceil(N/2)

    a, b = arr
    print(f"Case #{tc}:", "Alice" if a > b else "Bob")
