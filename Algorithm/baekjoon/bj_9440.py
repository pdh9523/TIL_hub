while True:
    N = input()
    if N == '0': break
    arr = sorted(N.split()[1:])
    a, b = "",""
    for i in range(len(arr)):
        if arr[i] != '0':
            a, b = arr[i], arr[i+1]
            arr = arr[:i] + arr[i+2:]
            break
    for i in range(0, len(arr), 2):
        a += arr[i]
        if i < len(arr) - 1:
            b += arr[i+1]

    print(int(a) + int(b))