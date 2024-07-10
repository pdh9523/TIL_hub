def div(num):
    arr,brr = [],[]
    for i in range(2, int(num**0.5) + 1):
        if num != i and num % i == 0:
            arr.append(i)
            arr.append(num // i)
            brr.append(i)
            brr.append(num // i)
            return arr, brr
    return arr, brr

c1, c2, c3, c4, c5, c6 = map(int, input().split())

x1, x2 = div(c1)
x6, x7 = div(c3)
_, x3 = div(c5)
_, x5 = div(c6)

for a in x1:
    for b in x2:
        for c in x3:
            for d in x5:
                for e in x6:
                    for f in x7:
                        if (a * b == c1 and
                            e * f == c3 and
                            b * c == c5 and
                            d * e == c6):
                            exit(print(a, b, c, d, e, f))
                            
