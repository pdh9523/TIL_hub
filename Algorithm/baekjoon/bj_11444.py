N = int(input())

fibo = [1,1]
for i in range(N):
    fibo.append((fibo[-1]+fibo[-2])%1000000007)

print(fibo[-1])