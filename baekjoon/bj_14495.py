def fibol (n):
    rem = {
        1: 1,
        2: 1,
        3: 1}
    if n > 3:
        for i in range(4, n+1):
            rem[i] = rem[i-1] + rem[i-3]
    return rem[n]

print(fibol(int(input())))