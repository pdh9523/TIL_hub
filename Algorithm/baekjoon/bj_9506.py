while True :
    a= int(input())
    if a == -1 :
        break
    else : 
        c = []
        for i in range(1,a) :
            if a % i == 0 : 
                c.append(i)
        if sum(c) == a :
            print(f"{a} = ", end="")
            print(*c, sep=" + ")
        else : 
            print(f"{a} is NOT perfect.")