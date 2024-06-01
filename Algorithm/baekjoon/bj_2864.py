arr = input().split()

for a,b in "65","56":
    print(sum(map(lambda x : int(x.replace(a,b)),arr)), end=" ")