for tc in range(1,int(input())+1):
    data = dict()
    for _ in range(int(input())):
        d = input()
        data[d] = data.get(d,0)+1
    print(f"#{tc}")
    for char in sorted(data, key = lambda x : (len(x),x)):
        print(char)