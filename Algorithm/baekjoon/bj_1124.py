N,M = map(int,input().split())

isprime = [True] * (M+1)
isprime[0]=isprime[1]=False
primes=[]
for i in range(2,M+1):
    if isprime[i]:
        primes.append(i)
        for j in range(i*i,M+1,i):
            isprime[j] = False

prime_cnt = [0]*(M+1)

for prime in primes:
    for i in range(prime,M+1,prime):
        tmp = i
        while not tmp%prime:
            prime_cnt[i]+=1
            tmp //=prime

ans = 0
for num in range(N,M+1):
    if isprime[prime_cnt[num]]:
        ans += 1
print(ans)