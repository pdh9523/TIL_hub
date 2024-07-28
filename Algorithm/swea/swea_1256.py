for _ in range(int(input())):

    N = int(input())
    text = input()[::-1]
    arr = []
    for idx in range(len(text)):
        arr.append(text[-idx:])
    
    arr.sort()

    print(arr[N-1])