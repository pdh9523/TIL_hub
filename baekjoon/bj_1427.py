a = list(input())
a.sort(key= lambda x: int(x), reverse = True)

print(*a, sep="")