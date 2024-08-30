N = int(input())
arr = input().split()

data = set()
for char in arr:
    if char[-6:] == "Cheese":
        data.add(char)

    if len(data) >=4 :
        exit(print("yummy"))
print("sad")