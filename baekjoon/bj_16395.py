a, b = map(int, input().split())
if b == 1 or a == b:
    print(1)
else :
    a -= 1
    b -= 1
    result_a = a
    result_b = b
    for a_count in range(1, b):
        result_a *= (a - a_count)

    for b_count in range(1, b):
        result_b *= (b - b_count)

    print(int(result_a/result_b))