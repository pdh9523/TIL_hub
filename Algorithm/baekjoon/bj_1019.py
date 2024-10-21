# 10씩 나누면서 자리수를 증가시키면 됨
N = int(input())
arr = [0]*10
num = 1

while N>0:

    while N%10 != 9:
        for i in str(N):
            arr[int(i)] += num
        N -= 1
    
    for i in range(min(N+1,10)):
        arr[i] += (N//10+1) * num
    
    arr[0] -= num
    num *= 10
    N //= 10

print(*arr)