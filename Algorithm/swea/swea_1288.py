for tc in range(int(input())):
    bit = 0
    number = int(input())
    target = number
    while True:
        for i in str(target):
            bit |= 1<<(int(i))
        if bit == (1<<10)-1:
            break
        target += number

    print(target)