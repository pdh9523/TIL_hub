while True :
    a = list(map(int,input().split()))
    b = set(a)
    
    
    if len(b) == 1:
        if b == {0} :
            break
        else :
            print("Equilateral")
    if len(b) == 2:
        if max(a) >= (sum(a))-max(a) :
            print("Invalid")
        else :
            print("Isosceles")
    if len(b) == 3:
        if max(a) >= (sum(a)-max(a)) :
            print("Invalid")
        else :
            print("Scalene")
