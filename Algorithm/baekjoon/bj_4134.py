def is_prime(num):
    if num < 2: return False
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
    return True


for _ in range(int(input())):
    N = int(input())
    while True:
        if is_prime(N): break
        N += 1
    print(N)