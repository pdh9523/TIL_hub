def cg(a) :
    if a == 0 :
        return 2
    else : 
        return cg(a-1)*2 - 1

a = int(input())
print(cg(a)**2)