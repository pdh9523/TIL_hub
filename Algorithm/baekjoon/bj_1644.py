N = int(input())
is_prime=[True]*(N+1)
sosu = []

for i in range(2,N+1):
    if is_prime[i]:
        sosu.append(i)
        tmp = 2*i
        while tmp <= N :
            is_prime[tmp]=False
            tmp += i
start,end,res,cnt=0,0,0,0
length=len(sosu)

if sosu and sosu[-1] == N :
    cnt += 1

while end < length:
    if res==N:
        cnt += 1
    
    if res <N:
        res+=sosu[end]
        end += 1
    else :
        res -= sosu[start]
        start += 1
print(cnt)