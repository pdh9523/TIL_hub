t = int(input())

for i in range(t):
    tc = int(input())
    
    for j in range(1,tc+1):
        print(j, end= " ")
        if j**3 == tc :
            print(f"#{i+1} {j}")
            break
        elif j**3 > tc:
            print(f"#{i+1} -1")
            break
    