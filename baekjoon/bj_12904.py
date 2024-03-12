S,T =list(input()), list(input())

while T!=S:
    if T.pop()=="B":    
        T.reverse()
    if not T:
        exit(print(0))
else:
    print(1)