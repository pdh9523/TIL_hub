for _ in range(int(input())):
    idx = 0
    text = input()
    ans = []
    length = 0
    for char in text :
        if char == "<":
            if idx > 0 :
                idx-=1
        elif char == ">":
            if idx < length :
                idx += 1
        elif char == "-":
            ans.pop()
            length-=1
        else :
            ans.insert(idx,char)
            idx+=1
    print(ans)