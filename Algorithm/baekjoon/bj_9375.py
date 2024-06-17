for _ in range(int(input())):
    data = dict()
    for _ in range(int(input())):
        name,category = input().split()
        data[category] = data.get(category,[]) + [name]

    res = [len(i) for i in data.values()]
    ans = 1
    for i in res :
        ans *= (i+1)
    print(ans-1)