t = int(input())
print(eval("".join([input() for _ in range(2*t-1)]).replace("/", "//")))