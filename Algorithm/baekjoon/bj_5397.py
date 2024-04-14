for _ in range(int(input())):
    text=input()
    ans=[]
    tmp=[]
    for char in text :
        if char == ">":
            if tmp : ans.append(tmp.pop())
        elif char == "<":
            if ans : tmp.append(ans.pop())
        elif char == "-": 
            if ans : ans.pop()
        else : ans.append(char)

    print(*(ans+tmp[::-1]), sep="")