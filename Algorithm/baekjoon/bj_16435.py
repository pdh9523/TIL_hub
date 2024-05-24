N, size = map(int,input().split())
fruits = sorted(list(map(int,input().split())), reverse=True)
while fruits :
    fruit = fruits.pop()
    if size >= fruit: size += 1
    else : break
print(size)        