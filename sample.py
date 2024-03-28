while 1:
    data = list(map(str, input().split('.')))
    print(data)
    data.pop()
    if data == ['']:
        exit()