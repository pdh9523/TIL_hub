a = int(input())

search = int(a * 0.9)

target = search + sum(list(map(int,str(search))))

while target != a :
    search -= 1 
    target = search + sum(list(map(int,str(search))))

print(search)