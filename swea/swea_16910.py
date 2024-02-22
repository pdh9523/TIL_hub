t = int(input())

for idx in range(t):
    tc = int(input())

    count = 0 
    for i in range(-tc,tc+1):
        for j in range(-tc,tc+1):
            if tc**2 >= i**2+j**2:
                count += 1
    print(f"#{idx+1} {count}")