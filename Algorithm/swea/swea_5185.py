t = int(input())

for idx in range(t):
    size, num = input().split()
    print(f"#{idx+1}", end=" ")
    for char in num:
        print(f"{int(char, base=16):04b}", end="")
    print()

